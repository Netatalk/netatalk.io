import os
import re
import markdown
from markdown.extensions.toc import TocExtension

from common import (
    VERSION,
    LOCALES,
    html_head,
    html_menlinks,
    html_navbar,
    html_foot,
)


# Generate manual

for lang in LOCALES:
    navbar = ""
    files = []
    base_url = f"/manual/{lang}/"
    with open(f"./manual/{lang}/_Sidebar.md", "r", encoding="utf-8") as input_file:
        text = input_file.read()
        html = markdown.markdown(
            text,
            extensions=[
                'fenced_code',
                'smarty',
                'tables',
            ],
        )

        navbar = f"""<div id="navbars">
    <div class="navbar">
    <h2>Table of contents</h2>
    {html}
    </div></div>
    """

    for file in os.listdir(f"./manual/{lang}/"):
        if file.endswith(".md"):
            files.append(f"{file}")
    for file in files:
        if file == "_Sidebar.md":
            continue
        with open(f"./manual/{lang}/{file}", "r", encoding="utf-8") as input_file:
            text = input_file.read()
            text = f"**Netatalk {VERSION}**\n\n[TOC]\n\n" + text
            html = markdown.markdown(
                text,
                extensions=[
                    'fenced_code',
                    'smarty',
                    'tables',
                    TocExtension(
                        anchorlink=True,
                    ),
                ],
            )
        page_title = file.replace('index', 'Index').replace('.md', '')
        new_name = file.replace('.md', '.html')

        with open(f"./public/manual/{lang}/{new_name}", "w", encoding="utf-8", errors="xmlcharrefreplace") as output_file:
            output_file.write(html_head(f"Netatalk Manual - {page_title}", f"manual/{lang}/{new_name}", lang))
            output_file.write("<body>\n")
            output_file.write(html_menlinks())
            output_file.write(navbar)
            output_file.write("<div id=\"content\">")
            output_file.write(html)
            output_file.write("</div>")
            output_file.write(html_foot(f"manual/{lang}/{new_name}"))

        print(f"Converted: {lang}/{file}")


# Generate READMEs

files = []

for file in os.listdir("./manual/"):
    if file.endswith(".md"):
        files.append(f"{file}")
for file in files:
    with open(f"./manual/{file}", "r", encoding="utf-8") as input_file:
        text = input_file.read()
        text = re.sub(r"\s<[^<>]+@[a-zA-Z0-9._-]+>", "", text)
        html = markdown.markdown(
            text,
            extensions=[
                'fenced_code',
                'smarty',
                'tables',
            ],
        )
    page_title = file.replace('index', 'Index').replace('.md', '')
    new_name = file.replace('.md', '.html').lower()

    with open(f"./public/{new_name}", "w", encoding="utf-8", errors="xmlcharrefreplace") as output_file:
        output_file.write(html_head(f"Netatalk - {page_title.capitalize()}", new_name, "en"))
        output_file.write("<body>\n")
        output_file.write(html_menlinks())
        output_file.write(html_navbar(VERSION))
        output_file.write("<div id=\"content\">")
        output_file.write(html)
        output_file.write("</div>")
        output_file.write(html_foot(f"{new_name}"))

    print(f"Converted: {new_name}")
