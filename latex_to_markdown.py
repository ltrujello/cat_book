import re
import yaml
from pathlib import Path
import tempfile
import subprocess

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

# tikz regex
center_env = re.compile("(\\\\begin{center}([\s\S]*?)\\\\end{center})")
tikz_stmt = re.compile("\\\\begin{tikzpicture}([\s\S]*?)\\\\end{tikzpicture}")
tikz_cd_stmt = re.compile("\\\\begin{tikzcd}([\s\S]*?)\\\\end{tikzcd}")

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

COMPILE = True
def compile_tikz_blocks(raw_tikz_code: str, chapter_num:int, section_num:int, figure_num:int):
    print(f"Working on {chapter_num=} {section_num=} {figure_num=}")
    if not COMPILE:
        return 

    pdf_destination = Path(f"docs/pdf/chapter_{chapter_num}/section_{section_num}_figure_{figure_num}.pdf")
    if pdf_destination.exists():
        return

    with tempfile.TemporaryDirectory() as tmpdirname:
        with open(f"tikz_template.tex") as f:
            tikz_code = f.read()

        tikz_code = re.sub("fillme", lambda x: raw_tikz_code, tikz_code)

        with open(f"{tmpdirname}/tikz_code.tex", "w") as f:
            f.write(tikz_code)

        with open(f"docs/tikz/chapter_{chapter_num}/tikz_code_{section_num}_{figure_num}.tex", "w") as f:
            f.write(tikz_code)

        proc_res = subprocess.run(
            f"latexmk -pdf -quiet -output-directory={tmpdirname} {tmpdirname}/tikz_code.tex",
            shell=True,
        )
        if proc_res.returncode != 0:
            print(f"Experience an error while processing docs/tikz/chapter_{chapter_num}/tikz_code_{section_num}_{figure_num}.tex")

        pdf_file = Path(f"{tmpdirname}/tikz_code.pdf")
        pdf_file.replace(pdf_destination)
        print("replaced bitch")
        print(tmpdirname)


def repl_center_env(match, chapter, section, ind):
    code = match.group(0)
    tikz_code_match = re.search(tikz_stmt, code)
    tikz_cd_code_match = re.search(tikz_cd_stmt, code)
    if tikz_code_match is None and tikz_cd_code_match is None:
        print(f"Found a center environment but it contains no tikz code, returning {code=}")
        return code, False
    compile_tikz_blocks(code, chapter, section, ind)
    img_url = f"\n<img src=\"../../png/chapter_{chapter}/section_{section}_figure_{ind}.png\" width=\"99%\" style=\"display: block; margin-left: auto; margin-right: auto;\"/>\n"

    return img_url, True

def clean_code(code: str, chapter:int, section: int) -> str:
    print(f"doing {chapter=} {section=}")
    # remove comments
    code = re.sub(tex_comment, "", code)

    new_code = code
    ind = 0
    num_figures = 0
    center_env_match = re.search(center_env, new_code)
    while center_env_match is not None:
        i = ind + center_env_match.start() - 1
        replaced_code, updated = repl_center_env(center_env_match, chapter, section, num_figures)
        j = ind + center_env_match.end() + 1

        # look for next instance of \begin{center} before updating new_code
        center_env_match = re.search(center_env, new_code[j:])
        # update new code
        new_code = new_code[:i] + replaced_code + new_code[j:]
        ind = i + len(replaced_code) + 1
        if updated:
            num_figures += 1
    # get rid of labels for now. alg might be chopping off leading backslash after label.
    new_code = re.sub(label_stmt, "", new_code)
    new_code = re.sub(label_stmt2, "", new_code)

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


def find_image_start_boundary(img_data):
    ind = 0
    while ind < len(img_data):
        row = img_data[ind]
        found = False
        for col in row:
            if col < 255:
                print(ind)
                found = True
                break
        if found:
            break
        ind += 1
    return ind

def find_image_end_boundary(img_data):
    ind = len(img_data) - 1
    while ind > 0:
        row = img_data[ind]
        found = False
        for col in row:
            if col < 255:
                print(ind)
                found = True
                break
        if found:
            break
        ind -= 1
    return ind

def convert_pdf_to_png(pdf_file):
    pdf_file = Path(pdf_file)
    chapter_dir = pdf_file.parts[-2]
    png_filename = Path(pdf_file.parts[-1]).with_suffix(".png")
    png_destination = Path(f"docs/png/{chapter_dir}/{png_filename}")
    print(png_destination.resolve())

    pdf_fp = str(pdf_file.resolve())
    page_pngs = convert_from_path(pdf_fp)

    # Create the png of the pdf
    total = len(page_pngs)
    ind = 0
    if total > 1:
        print(f"WARNING! {pdf_file=} has more than two pages, expected only one. Going to use"
              " the last page. ")
        ind = len(page_pngs) - 1

    page_pngs = list(page_pngs)
    image = page_pngs[ind]
    print(f"Converting page {ind}/{total}")
    # easier to find boundaries of a grayscale image
    grayscale_image = image.convert("L")
    img_data = np.asarray(grayscale_image)
    y_0 = find_image_start_boundary(img_data)
    y_1 = find_image_end_boundary(img_data)
    x_0 = find_image_start_boundary(img_data.T)
    x_1 = find_image_end_boundary(img_data.T)
    horizontal_len = len(img_data.T)
    x_0 = int(min(.20*horizontal_len, x_0))
    x_1 = int(max(.80*horizontal_len, x_1))
    
    true_img = image.convert("RGB")
    img_data = np.asarray(true_img)
    cropped_img_data= img_data[y_0:y_1, x_0:x_1]
    cropped_img = Image.fromarray(np.uint8(cropped_img_data))
    cropped_img.save(str(png_destination), "PNG")

        
    # png -> np.array
    # numpy.asarray(PIL.Image.open('test.jpg'))

    # np.array -> img
    # Image.fromarray(np.uint8(img_data))

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
