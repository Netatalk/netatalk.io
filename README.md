# netatalk.io

Netatalk static website.

The core website is generated from Markdown sources using Python scripts in `scripts/`,
orchestrated by the `build.sh` shell script.

Release notes as well as wiki documentation sources are fetched remotely
from the Netatalk/netatalk GitHub project by the build script,
and not kept under revision control in this repository.

The rest of the documentation sources are created on the fly by the netatalk build system,
which exists as a submodule in this repository and called by the build script.

## New release procedure

- Create a news story at the top of `archive.md` (the top three stories will be substituted to `index.md`.)
- Prepend the release version to the VERSIONS list in `scripts/common.py`.
- cd to the `netatalk` submodule, fetch from origin and checkout the release tag, e.g. `git checkout 4.5.0`.
- Test the updates by running the `build.sh` script, passing a GITHUB_TOKEN env variable with a valid GitHub API token.
- Commit all above changes and push to remote git to publish to web hosting.

When introducing a new *minor* release series, you also need to create a new public subdir with a `.gitkeep` file,
e.g. `public/4.4/.gitkeep`.
