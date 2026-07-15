# netatalk.io

The static website of the Netatalk project, generated from Markdown sources by a custom Python script.

- `assets/` sundry downloadable files that don't fit anywhere else
- `css/` stylesheets used by the website
- `gfx/` image files used inline in html pages
- `logo/` the canonical Netatalk logo images, not used directly by the website
- `pages/` the top level website pages Markdown sources
- `releasenotes/` historical static release notes in Markdown format
- `scripts/` Python scripts that build the website
- `security/` vulnerability advisories in Markdown, and raw patches
- `spec/` specification documentation in Markdown
- `templates/` reusable HTML fragments used by the website generators

Later release notes as well as wiki documentation Markdown sources are fetched on the fly
from the *Netatalk/netatalk* GitHub project by the build script.

The rest of the Markdown sources are created by the netatalk build system,
which exists as a submodule in this repository and called by the build script.
It also builds Doxygen documentation for the C source code.

## Building the website

The Markdown sources are converted to HTML using Python scripts in `scripts/`,
orchestrated by the `build.sh` shell script, and output to the `public/` directory.
A GitHub personal access token is required to fetch release notes from the GitHub API.
Without a token, the build script will skip fetching release notes and the generated website will be incomplete.

```sh
GITHUB_TOKEN=your_token ./build.sh
```

To build the website for local review and start a static web server:

```sh
GITHUB_TOKEN=your_token ./build.sh test
```

This generates internal website URLs with `http://127.0.0.1:8000/` as the base URL
and serves the generated site from `public/`. Use `--host`, `--port`, or `--base-url`
to customize the local server and generated base URL, for example:

```sh
GITHUB_TOKEN=your_token ./build.sh test --host 0.0.0.0 --port 8080 --base-url http://localhost:8080/
```

The default production base URL is `https://netatalk.io/`. It can also be overridden
for any build by setting `NETATALK_SITE_BASE_URL`.

## New release procedure

- Create a news story at the top of `pages/archive.md` (the top three stories will be substituted to `pages/index.md`.)
- Prepend the release version to the VERSIONS list in `scripts/common.py`.
- cd to the `netatalk` submodule, fetch from origin and checkout the release tag, e.g. `git checkout 4.5.0`.
- Test the updates by running `./build.sh test` and reviewing the generated site.
- Commit all above changes and push to remote git to publish to web hosting.
