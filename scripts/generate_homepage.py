import os
import re
import markdown

from common import (
    VERSION,
    VERSIONS,
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

            if dir == "." and file == "index.md":
                with open("archive.md", "r", encoding="utf-8") as archive_file:
                    lines = archive_file.readlines()
                    news_indices = [i for i, line in enumerate(lines) if line.startswith("### ")]
                    if len(news_indices) > 0:
                        start_idx = news_indices[0]
                        end_idx = news_indices[3] if len(news_indices) >= 4 else len(lines)
                        news_content = "".join(lines[start_idx:end_idx])
                        text = text.replace("NETATALK_NEWS", news_content)

            if dir == "." and file == "documentation.md":
                v4_links = []
                for v in VERSIONS:
                    if v.startswith("4"):
                        minor = re.search(r"^(\d+\.\d+)", v).group()
                        v4_links.append(f"- [Netatalk {v}](/{minor}/ReleaseNotes{v}.html)")
                text = text.replace("NETATALK_V4_RELEASE_NOTES", "\n".join(v4_links))

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
            output_file.write("<body>\n")
            output_file.write(html_menlinks())
            output_file.write(html_navbar(VERSION))
            output_file.write("<div id=\"content\">\n")
            output_file.write(html)
            output_file.write("</div>\n")
            output_file.write(html_foot(new_path))

        print(f"Converted: {file}")
