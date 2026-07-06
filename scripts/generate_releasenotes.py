import os
import re
import sys
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


if os.environ.get("GITHUB_TOKEN") is None:
    print("WARNING: No GitHub token found. Skipping release notes generation.")
else:
    github_token = os.environ["GITHUB_TOKEN"]
    for release_version in VERSIONS:
        github_tag = "netatalk-" + release_version.replace(".", "-")
        minor_version = re.search(r"^(\d+\.\d+)", release_version).group()
        file_name = f"ReleaseNotes{release_version}.html"
        url = f"https://api.github.com/repos/Netatalk/netatalk/releases/tags/{github_tag}"

        headers = {
            "Accept": "application/vnd.github+json",
            "Authorization": "Bearer " + github_token,
            "X-GitHub-Api-Version": "2022-11-28",
        }

        response = requests.get(url, headers=headers)
        if response.status_code == 401:
            print(f"ERROR: GitHub authentication failed (HTTP 401). Check your GITHUB_TOKEN.")
            sys.exit(1)
        if response.status_code != 200:
            print(f"Skipping {release_version}: HTTP {response.status_code} for tag {github_tag}")
            continue
        body = response.json()
        published_at = re.search(r"^(\d{4}-\d{2}-\d{2})", body["published_at"]).group()

        body_text = github_pr_url_pattern.sub(r'[#\1](https://github.com/Netatalk/netatalk/pull/\1)', body["body"])
        html = markdown.markdown(
            body_text,
            extensions=['fenced_code', 'smarty', 'tables'],
            output_format='html',
        )

        html = localize_internal_site_urls(html)
        html = url_pattern.sub(r" <a href='\2'>\2</a>", html)
        html = github_pattern.sub(r"<a href='https://github.com/Netatalk/netatalk/issues/\2'>\1\2</a>", html)

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

        pre_footer = f"""{downloads_html}<h1>Footnotes</h1>
<p>Release published on {published_at}</p>
<p>Generated from <a href=\"https://github.com/Netatalk/netatalk/releases/tag/{github_tag}\">GitHub Release Notes</a></p>
</div>
"""

        with open(f"./public/{minor_version}/{file_name}", "w", encoding="utf-8", errors="xmlcharrefreplace") as output_file:
            output_file.write(html_head(f"Netatalk Release Notes - {release_version}", f"{minor_version}/{file_name}"))
            output_file.write("<body>\n")
            output_file.write(html_menlinks())
            output_file.write(html_navbar(VERSION))
            output_file.write("<div id=\"content\">\n")
            output_file.write(html)
            output_file.write(pre_footer)
            output_file.write(html_foot(f"{minor_version}/{file_name}"))

            print(f"Converted: {file_name}")
