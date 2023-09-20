import re
import yaml
from pathlib import Path

begin_document = re.compile("\\\\begin{document}")
end_document = re.compile("\\\\end{document}")
chapter = re.compile(r"\\chapter{(.*?)}")
section = re.compile(r"\\section{(.*?)}")
textbf = re.compile("\\\\textbf{(.*?)}")
textit = re.compile("\\\\textit{(.*?)}")
emph_cmd = re.compile("\\\\emph{(.*?)}")
latex_quotes = re.compile("``(.*?)''")
display_math = re.compile("(\\\\\\[([\s\S]*?)\\\\\\])")
align_stmt = re.compile("(\\\\begin{align}([\s\S]*?)\\\\end{align})")
align_star_stmt = re.compile("(\\\\begin{align\*}([\s\S]*?)\\\\end{align\*})")
gather_env = re.compile("(\\\\begin{gather}([\s\S]*?)\\\\end{gather})")
gather_star_env = re.compile("(\\\\begin{gather\*}([\s\S]*?)\\\\end{gather\*})")
newpage_cmd = re.compile("\\\\newpage")
tabular_env = re.compile("\\\\begin{tabular}([\s\S]*?)\\\\end{tabular}")
indent_space = re.compile("^\\s*")

itemize_env = re.compile("\\\\begin{itemize}([\s\S]*?)\\\\end{itemize}")

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


def repl_tabular_env(match):
    contents = match.group(1)
    contents = re.sub("\\\\hline", "", contents)
    # find the index 
    num_brackets_seen = 0
    j = 0
    for ind, ch in enumerate(contents):
        if ch == "{":
            num_brackets_seen += 1
        elif ch == "}":
            num_brackets_seen -= 1
            if num_brackets_seen == 0:
                j = ind + 1
                break
    rows = []
    while j < len(contents):
        code = contents[j:]
        ind = 0
        row = []
        while True:
            curr_match = re.search(ampersand, code[ind:])
            next_match = re.search("\\\\\\\\", code[ind:])
            if curr_match is not None and next_match is not None:
                if next_match.start() < curr_match.start():
                    curr_match = None

            if curr_match is not None:
                row.append(re.sub("\\n", " ", code[ind: ind + curr_match.start()]))
                ind += curr_match.end() + 1
                continue
            else:
                curr_match = re.search("\\\\\\\\", code[ind:])
                if curr_match is not None:
                    row.append(re.sub("\\n", " ", code[ind: ind + curr_match.start()]))
                    # update index in the outer while loop
                    j += ind + curr_match.end() + 1
                else:
                    curr_match = re.search(end_tabular_env, code[ind:])
                    if curr_match is not None:
                    else:
                        print(f"Warning: failed to find an ampersand or \\\\\\\\ in {code[ind:]}")
                    j = len(contents)
                break
        rows.append(row)

    output = "\n"
    first_row = rows[0]
    output += "|"
    output += "|".join(first_row)
    output += "|\n"

    for elem in first_row:
        output += "|"
        output += "-"*len(elem)
    output += "|\n"

    for row in rows[1:]:
        output += "|"
        output += "|".join(row)
        output += "|\n"
    return output

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


    # replace latex bolding with ** syntax
    new_code = re.sub(textbf, "**\\1**", new_code)
    # replace latex bolding with * syntax
    new_code = re.sub(emph_cmd, "*\\1*", new_code)
    new_code = re.sub(textit, "*\\1*", new_code)
    # replace latex quotes with " syntax
    new_code = re.sub(latex_quotes, "\"\\1\"", new_code)
    # set display math on newlines
    new_code = re.sub(display_math, "\n\\1\n", new_code)
    # set align environments on newlines
    new_code = re.sub(align_stmt, "\n\\1\n", new_code)
    # set align* environments on newlines 
    new_code = re.sub(align_star_stmt, "\n\\1\n", new_code)
    # set gather environments on newlines
    new_code = re.sub(gather_env, "\n\\1\n", new_code)
    # set gather environments on newlines
    new_code = re.sub(gather_star_env, "\n\\1\n", new_code)
    # replace itemize environments
    new_code = re.sub(itemize_env, repl_itemize_env, new_code)
    # remove \newpage
    new_code = re.sub(newpage_cmd, "", new_code)
    # replace tabular environments with markdown tables
    new_code = re.sub(tabular_env, repl_tabular_env, new_code)

    # de indent everything
    final_code = ""
    for line in new_code.split("\n"):
        final_code += re.sub(indent_space, "", line)
        final_code += "\n"
    return final_code

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
