import os
import re
import markdown
import requests

from common import (
    VERSIONS,
    VERSION,
    html_head,
    html_menlinks,
    html_navbar,
    html_foot,
)

url_pattern = re.compile(r'((?:^|\s)(https?://\S+)(?=<))')
github_pattern = re.compile(r'(GitHub #)(\d+)')


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
        body = response.json()
        published_at = re.search(r"^(\d{4}-\d{2}-\d{2})", body["published_at"]).group()

        html = markdown.markdown(body["body"], extensions=['fenced_code', 'smarty', 'tables'])

        html = url_pattern.sub(r" <a href='\2'>\2</a>", html)
        html = github_pattern.sub(r"<a href='https://github.com/Netatalk/netatalk/issues/\2'>\1\2</a>", html)

        pre_footer = f"""<h1>Footnotes</h1>
<p>Release published on {published_at}</p>
<p>Generated from <a href=\"https://github.com/Netatalk/netatalk/releases/tag/{github_tag}\">GitHub Release Notes</a></p>
</div>
"""

        with open(f"./public/{minor_version}/{file_name}", "w", encoding="utf-8", errors="xmlcharrefreplace") as output_file:
            output_file.write(html_head(f"Netatalk Release Notes - {release_version}", f"{minor_version}/{file_name}"))
            output_file.write(html_menlinks())
            output_file.write(html_navbar(VERSION))
            output_file.write("<div id=\"content\">\n")
            output_file.write(html)
            output_file.write(pre_footer)
            output_file.write(html_foot(f"{minor_version}/{file_name}"))

            print(f"Converted: {file_name}")
