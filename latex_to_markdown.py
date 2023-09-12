import re
import yaml

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
