import os
import re
import sys
import markdown
import requests

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
        if version_match is None:
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


def github_release_assets(release_version, github_token):
    github_tag = "netatalk-" + release_version.replace(".", "-")
    url = f"https://api.github.com/repos/Netatalk/netatalk/releases/tags/{github_tag}"
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": "Bearer " + github_token,
        "X-GitHub-Api-Version": "2022-11-28",
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 401:
        print("ERROR: GitHub authentication failed (HTTP 401). Check your GITHUB_TOKEN.")
        sys.exit(1)
    if response.status_code != 200:
        print(f"Skipping downloads: HTTP {response.status_code} for tag {github_tag}")
        return []

    return response.json().get("assets", [])


def download_links(assets):
    if not assets:
        return ""

    links = [
        f"- [{asset['name']}]({asset['browser_download_url']})"
        for asset in assets
    ]
    return "\n".join(links) + "\n"

subdirs = [
    'security',
    'spec',
]

page_subdirs = [
    ('pages', '.'),
]

# Historical release notes; later ones are built in generate_releasenotes.py
release_note_subdirs = [
    '1.3',
    '1.5',
    '1.6',
    '2.0',
    '2.1',
    '2.2',
    '3.0',
    '3.1',
]

pages = [(dir, dir) for dir in subdirs]
pages.extend(page_subdirs)
pages.extend((f"releasenotes/{dir}", dir) for dir in release_note_subdirs)

github_token = os.environ.get("GITHUB_TOKEN")
download_assets = github_release_assets(VERSION, github_token) if github_token else []

for source_dir, output_dir in pages:
    files = []

    for file in os.listdir(source_dir):
        if file.endswith(".md") and file != "README.md":
            files.append(f"{file}")
    for file in files:
        with open(f"./{source_dir}/{file}", "r", encoding="utf-8") as input_file:
            text = input_file.read()

            if source_dir == "pages" and file == "index.md":
                with open("pages/archive.md", "r", encoding="utf-8") as archive_file:
                    lines = archive_file.readlines()
                    news_indices = [i for i, line in enumerate(lines) if line.startswith("### ")]
                    if len(news_indices) > 0:
                        start_idx = news_indices[0]
                        end_idx = news_indices[3] if len(news_indices) >= 4 else len(lines)
                        news_content = "".join(lines[start_idx:end_idx])
                        text = text.replace("NETATALK_NEWS", news_content)

            text = text.replace("NETATALK_RELEASE_NOTES", release_notes_index())
            if source_dir == "pages" and file == "download.md":
                text = text.replace("NETATALK_DOWNLOADS", download_links(download_assets))

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

        new_path = f"{output_dir}/{new_name}"
        if output_dir == ".":
            new_path = new_name
        os.makedirs(os.path.dirname(f"./public/{new_path}") or "./public", exist_ok=True)
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
