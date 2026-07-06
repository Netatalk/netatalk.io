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
    js_mermaid,
    localize_internal_site_urls,
    site_url,
)

def release_notes_index():
    versions_by_minor = {}
    for version in VERSIONS:
        version_match = re.search(r"^(\d+)\.(\d+)", version)
        if version_match is None or int(version_match.group(1)) < 4:
            continue
        minor = version_match.group()
        versions_by_minor.setdefault(minor, []).append(version)

    sections = []
    for minor, versions in versions_by_minor.items():
        links = [f"[{version}]({site_url(f'{minor}/ReleaseNotes{version}.html')})" for version in versions]
        link_lines = []
        for i in range(0, len(links), 3):
            line = " · ".join(links[i:i + 3])
            if i + 3 < len(links):
                line += " ·"
            link_lines.append(line)
        sections.append(f"## {minor}\n\n" + "\n".join(link_lines))

    return "\n\n".join(sections)

subdirs = [
    '.',
    'security',
    'spec',
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
        if file.endswith(".md") and file != "README.md":
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

            text = text.replace("NETATALK_RELEASE_NOTES", release_notes_index())

            html = markdown.markdown(
                text,
                extensions=[
                    'fenced_code',
                    'smarty',
                    'tables',
                ],
                output_format='html',
            )
            html = localize_internal_site_urls(html)
            html = re.sub(r'<pre><code class="language-mermaid">(.*?)</code></pre>', r'<pre class="mermaid">\1</pre>', html, flags=re.DOTALL)
        new_name = file.replace('.md', '.html')
        h1_match = re.search(r'^# (.+)$', text, re.MULTILINE)
        if h1_match:
            page_title = h1_match.group(1)
        elif file == "index.md":
            page_title = "Networking Apple Macintosh through Open Source"
        else:
            page_title = file.replace('.md', '').replace('_', ' ').capitalize()

        new_path = f"{dir}/{new_name}"
        if dir == ".":
            new_path = new_name
        with open(f"./public/{new_path}", "w", encoding="utf-8", errors="xmlcharrefreplace") as output_file:
            output_file.write(html_head(f"Netatalk - {page_title}", new_path))
            output_file.write("<body>\n")
            output_file.write(js_mermaid())
            output_file.write(html_menlinks())
            output_file.write(html_navbar(VERSION))
            output_file.write("<div id=\"content\">\n")
            output_file.write(html)
            output_file.write("</div>\n")
            output_file.write(html_foot(new_path))

        print(f"Converted: {file}")
