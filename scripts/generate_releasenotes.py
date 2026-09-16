import os
import re
import sys
from pathlib import Path

import markdown
import requests

from common import (
    CLIENT_VERSIONS,
    VERSIONS,
    localize_internal_site_urls,
    render_page,
)

url_pattern = re.compile(r'((?:^|\s)(https?://\S+)(?=<))')
github_pattern = re.compile(r'(GitHub #)(\d+)')
release_notes_dir = Path(__file__).resolve().parents[1] / "releasenotes"
NETATALK_REPOSITORY = "Netatalk/netatalk"
CLIENT_REPOSITORY = "Netatalk/netatalk-client"


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


def github_release(release_version, github_token, repository, github_tag):
    url = f"https://api.github.com/repos/{repository}/releases/tags/{github_tag}"
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
    github_pr_url_pattern = re.compile(
        rf"https://github\.com/{re.escape(repository)}/pull/(\d+)"
    )
    body_text = github_pr_url_pattern.sub(
        rf'[#\1](https://github.com/{repository}/pull/\1)',
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
<p>Generated from <a href="https://github.com/{repository}/releases/tag/{github_tag}">GitHub Release Notes</a></p>
"""
    return body_text, post_content


def generate_release_notes(versions, repository, product_name, output_prefix="", static_notes=False):
    github_token = os.environ.get("GITHUB_TOKEN")

    for release_version in versions:
        minor_version = re.search(r"^(\d+\.\d+)", release_version).group()
        file_name = f"ReleaseNotes{release_version}.html"
        local_note = static_release_note(release_version, minor_version) if static_notes else None

        if local_note is not None:
            body_text = local_note.read_text(encoding="utf-8")
            post_content = ""
            source = local_note.relative_to(release_notes_dir.parent)
        else:
            if not github_token:
                print(f"Skipping {release_version}: no static release note and no GITHUB_TOKEN")
                continue

            github_tag = (
                "netatalk-" + release_version.replace(".", "-")
                if repository == NETATALK_REPOSITORY
                else release_version
            )
            release = github_release(release_version, github_token, repository, github_tag)
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
                rf"<a href='https://github.com/{repository}/issues/\2'>\1\2</a>",
                html,
            )

        output_dir = Path("public") / output_prefix / minor_version
        output_dir.mkdir(parents=True, exist_ok=True)
        output_path = Path(output_prefix) / minor_version / file_name
        with open(
            output_dir / file_name,
            "w",
            encoding="utf-8",
            errors="xmlcharrefreplace",
        ) as output_file:
            output_file.write(render_page(
                f"{product_name} Release Notes - {release_version}",
                str(output_path),
                html + post_content,
            ))

        print(f"Converted: {output_path} ({source})")


def main():
    generate_release_notes(
        VERSIONS, NETATALK_REPOSITORY, "Netatalk", static_notes=True
    )
    generate_release_notes(
        CLIENT_VERSIONS, CLIENT_REPOSITORY, "Netatalk Client", output_prefix="client"
    )


if __name__ == "__main__":
    main()
