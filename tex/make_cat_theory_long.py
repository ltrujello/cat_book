import re

include_stmt = re.compile("\\\\include{([\s\S]*?)}")
with open("cat_theory.tex") as f:
    contents = f.read()

def repl(match):
    file_path = f"{match.group(1)}.tex"
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

thing = re.sub(include_stmt, repl, contents)

with open("cat_theory_long.tex", "w") as f:
    f.write(thing)
