import re
import yaml
from pathlib import Path

begin_document = re.compile("\\\\begin{document}")
end_document = re.compile("\\\\end{document}")
chapter = re.compile(r"\\chapter{(.*?)}")
section = re.compile(r"\\section{(.*?)}")

# label statement
label_stmt = re.compile(r"\\label{(.*?)}")
label_stmt2 = re.compile(r"label{(.*?)}")

# amsthm environments
definition_stmt = re.compile("\\\\begin{definition}([\s\S]*?)\\\\end{definition}")
proposition_stmt = re.compile("\\\\begin{proposition}([\s\S]*?)\\\\end{proposition}")
lemma_stmt = re.compile("\\\\begin{lemma}([\s\S]*?)\\\\end{lemma}")
corollary_stmt = re.compile("\\\\begin{corollary}([\s\S]*?)\\\\end{corollary}")
theorem_stmt = re.compile("\\\\begin{theorem}([\s\S]*?)\\\\end{theorem}")
example_stmt = re.compile("\\\\begin{example}([\s\S]*?)\\\\end{example}")
description_stmt = re.compile("\\\\begin{example}([\s\S]*?)\\\\end{example}")
proof_stmt = re.compile("\\\\begin{prf}([\s\S]*?)\\\\end{prf}")


repl_def = lambda x: repl_asmthm_statement(x, "definition")
repl_prop = lambda x: repl_asmthm_statement(x, "proposition" )
repl_lemma = lambda x: repl_asmthm_statement(x, "lemma")
repl_corollary = lambda x: repl_asmthm_statement(x, "corollary")
repl_theorem = lambda x: repl_asmthm_statement(x, "theorem")
repl_example = lambda x: repl_asmthm_statement(x, "example")
repl_desc = lambda x: repl_asmthm_statement(x, "description")
repl_proof = lambda x: repl_asmthm_statement(x, "proof")


def repl_asmthm_statement(match, class_name):
    env_contents = match.group(1)
    env_contents = textwrap.dedent(env_contents)
    repl = f"\n<span style=\"display:block\" class=\"{class_name}\">{env_contents}</span>"
    return repl

def repl_itemize_env(match):
    code = match.group(0)

    items = []
    ind = 0
    while True:
        curr_match = re.search(item_stmt, code[ind:])
        next_match = re.search(item_stmt, code[ind + curr_match.end():])

        if next_match is not None:
            items.append(code[ind + curr_match.end():ind + curr_match.end() + next_match.start()])
            ind = ind + curr_match.end() + next_match.start()

        else:
            next_match = re.search(end_itemize_env, code[ind + curr_match.end():])
            if next_match is not None:
                items.append(code[ind + curr_match.end(): ind + curr_match.end() + next_match.start()])
            else:
                print(f"Failed to find \\item or \\end{{itemize}} in {code[ind + curr_match.end():]}")
            break
    res = "\n"
    for item in items:
        res += f"* {item}\n\n"
    return res



def clean_code(code: str, chapter:int, section: int) -> str:
    # remove comments
    code = re.sub(tex_comment, "", code)

    new_code = code
    ind = 0
    # get rid of labels for now. alg might be chopping off leading backslash after label.
    new_code = re.sub(label_stmt, "", new_code)
    new_code = re.sub(label_stmt2, "", new_code)

    # deindent the code
    new_code = textwrap.dedent(new_code)

    # amsthm env
    new_code = re.sub(definition_stmt, repl_def, new_code)
    new_code = re.sub(proposition_stmt, repl_prop, new_code)
    new_code = re.sub(lemma_stmt, repl_lemma, new_code)
    new_code = re.sub(corollary_stmt, repl_corollary, new_code)
    new_code = re.sub(theorem_stmt, repl_theorem, new_code)
    new_code = re.sub(example_stmt, repl_example, new_code)
    new_code = re.sub(description_stmt, repl_desc, new_code)
    new_code = re.sub(proof_stmt, repl_proof, new_code)

    return new_code

def latex_to_markdown():
    with open("tex/cat_theory_long.tex") as f:
        contents = f.read()

    begin_match = re.search(begin_document, contents)
    end_match = re.search(end_document, contents)

    tex_code = contents[begin_match.start() : end_match.start()]

    chapters = {}
    for chapter_match in re.finditer(chapter, tex_code):
        chapter_start = chapter_match.end() + 1
        chapter_name = chapter_match.group(1)
        next_chapter_match = re.search(chapter, tex_code[chapter_start:])
        if next_chapter_match is None:
            chapter_code = tex_code[chapter_start:]
        else:
            chapter_code = tex_code[chapter_start:chapter_start + next_chapter_match.start()]

        sections = {}
        chapters[chapter_name] = sections
        for section_match in re.finditer(section, chapter_code):
            section_start = section_match.end() + 1
            section_name = section_match.group(1)
            next_section_match = re.search(section, chapter_code[section_start:])
            if next_section_match is None:
                section_code = chapter_code[section_start:]
            else:
                section_code = chapter_code[section_start:section_start + next_section_match.start()]

            sections[section_name] = section_code

    chapter_num = 1
    for chapter_name, sections in chapters.items():
        chapter_dir = Path(f"docs/{chapter_name}")
        chapter_pdf_dir = Path(f"docs/pdf/chapter_{chapter_num}")
        chapter_png_dir = Path(f"docs/png/chapter_{chapter_num}")
        chapter_tikz_dir = Path(f"docs/tikz/chapter_{chapter_num}")
        chapter_dir.mkdir(exist_ok=True)
        chapter_pdf_dir.mkdir(exist_ok=True)
        chapter_png_dir.mkdir(exist_ok=True)
        chapter_tikz_dir.mkdir(exist_ok=True)

        section_num = 1
        for section_name, code in sections.items():
            with open(chapter_dir / f"{section_name}.md", "w") as f:
                code = clean_code(code, chapter_num, section_num)
                f.write(f"#{chapter_num}.{section_num}. {section_name}\n")
                f.write(code)
            section_num += 1
        chapter_num += 1
    create_mkdocs_yaml_nav(chapters)

def create_mkdocs_yaml_nav(chapters):
    nav = []
    chapter_num = 1
    for chapter in chapters:
        nav_chapter = {chapter: []}
        sections = chapters[chapter]
        section_num = 1
        for section_name in sections:
            nav_chapter[chapter].append({f"{chapter_num}.{section_num} {section_name}": f"{chapter}/{section_name}.md"})
            section_num += 1

       nav.append(nav_chapter)
        chapter_num += 1
    
    with open("mkdocs.yml") as f:
        yaml_contents = f.read()

    yaml_data = yaml.load(yaml_contents, Loader=yaml.Loader)
    yaml_data["nav"] = nav
    yaml_output = yaml.dump(yaml_data, Dumper=yaml.Dumper)

    with open("mkdocs.yml", "w") as f:
        f.write(yaml_output)

if __name__ == "__main__":
    latex_to_markdown()
