import os
import re
import sys
from pathlib import Path

import markdown
import requests

from common import (
    VERSIONS,
    VERSION,
    html_head,
    html_menlinks,
    html_navbar,
    html_foot,
    localize_internal_site_urls,
)

url_pattern = re.compile(r'((?:^|\s)(https?://\S+)(?=<))')
github_pattern = re.compile(r'(GitHub #)(\d+)')
github_pr_url_pattern = re.compile(r'https://github\.com/Netatalk/netatalk/pull/(\d+)')
release_notes_dir = Path(__file__).resolve().parents[1] / "releasenotes"


def static_release_note(release_version, minor_version):
    path = release_notes_dir / minor_version / f"ReleaseNotes{release_version}.md"
    if path.is_file():
        return path

    # Preserve historical short form release versions.
    if release_version == f"{minor_version}.0":
        path = release_notes_dir / minor_version / f"ReleaseNotes{minor_version}.md"
        if path.is_file():
            return path

    return None


def github_release(release_version, github_token):
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
        print(f"Skipping {release_version}: HTTP {response.status_code} for tag {github_tag}")
        return None

    body = response.json()
    published_at = re.search(r"^(\d{4}-\d{2}-\d{2})", body["published_at"]).group()
    body_text = github_pr_url_pattern.sub(
        r'[#\1](https://github.com/Netatalk/netatalk/pull/\1)',
        body["body"],
    )

    assets = body.get("assets", [])
    downloads_html = ""
    if assets:
        downloads_html = "<h1>Downloads</h1>\n<ul>\n"
        for asset in assets:
            name = asset["name"]
            download_url = asset["browser_download_url"]
            size_mb = asset["size"] / (1024 * 1024)
            downloads_html += f"<li><a href='{download_url}'>{name}</a> ({size_mb:.1f} MB)</li>\n"
        downloads_html += "</ul>\n"

    post_content = f"""{downloads_html}<h1>Footnotes</h1>
<p>Release published on {published_at}</p>
<p>Generated from <a href="https://github.com/Netatalk/netatalk/releases/tag/{github_tag}">GitHub Release Notes</a></p>
"""
    return body_text, post_content


def main():
    github_token = os.environ.get("GITHUB_TOKEN")

    for release_version in VERSIONS:
        minor_version = re.search(r"^(\d+\.\d+)", release_version).group()
        file_name = f"ReleaseNotes{release_version}.html"
        local_note = static_release_note(release_version, minor_version)

        if local_note is not None:
            body_text = local_note.read_text(encoding="utf-8")
            post_content = ""
            source = local_note.relative_to(release_notes_dir.parent)
        else:
            if not github_token:
                print(f"Skipping {release_version}: no static release note and no GITHUB_TOKEN")
                continue

            release = github_release(release_version, github_token)
            if release is None:
                continue
            body_text, post_content = release
            source = "GitHub"

        html = markdown.markdown(
            body_text,
            extensions=['fenced_code', 'smarty', 'tables'],
            output_format='html',
        )

        html = localize_internal_site_urls(html)
        if local_note is None:
            html = url_pattern.sub(r" <a href='\2'>\2</a>", html)
            html = github_pattern.sub(
                r"<a href='https://github.com/Netatalk/netatalk/issues/\2'>\1\2</a>",
                html,
            )

        os.makedirs(f"./public/{minor_version}", exist_ok=True)
        with open(
            f"./public/{minor_version}/{file_name}",
            "w",
            encoding="utf-8",
            errors="xmlcharrefreplace",
        ) as output_file:
            output_file.write(html_head(f"Netatalk Release Notes - {release_version}", f"{minor_version}/{file_name}"))
            output_file.write("<body>\n")
            output_file.write(html_menlinks())
            output_file.write(html_navbar(VERSION))
            output_file.write("<div id=\"content\">\n")
            output_file.write(html)
            output_file.write(post_content)
            output_file.write("</div>\n")
            output_file.write(html_foot(f"{minor_version}/{file_name}"))

        print(f"Converted: {file_name} ({source})")


if __name__ == "__main__":
    main()
