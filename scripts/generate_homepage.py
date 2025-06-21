import os
import markdown

from common import (
    VERSION,
    html_head,
    html_menlinks,
    html_navbar,
    html_foot,
)

subdirs = [
    '.',
    'blog',
    'security',
# Historical release notes; later ones are built in generate_releasenotes.py
    '1.3',
    '1.5',
    '1.6',
    '2.0',
    '2.1',
    '2.2',
    '3.0',
    '3.1',
]

for dir in subdirs:
    files = []

    for file in os.listdir(dir):
        if file.endswith(".md"):
            files.append(f"{file}")
    for file in files:
        path = f"{dir}/{file}"
        with open(f"./{dir}/{file}", "r", encoding="utf-8") as input_file:
            text = input_file.read()
            html = markdown.markdown(
                text,
                extensions=[
                    'fenced_code',
                    'smarty',
                    'tables',
                ],
            )
        page_title = file.replace('.md', '')
        new_name = file.replace('.md', '.html')
        if page_title == "index":
            page_title = "Networking Apple Macintosh through Open Source"
        else:
            page_title.capitalize()

        new_path = f"{dir}/{new_name}"
        if dir == ".":
            new_path = new_name
        with open(f"./public/{new_path}", "w", encoding="utf-8", errors="xmlcharrefreplace") as output_file:
            output_file.write(html_head(f"Netatalk - {page_title}", new_path))
            output_file.write(html_menlinks())
            output_file.write(html_navbar(VERSION))
            output_file.write("<div id=\"content\">\n")
            output_file.write(html)
            output_file.write("</div>\n")
            output_file.write(html_foot(new_path))

        print(f"Converted: {file}")
