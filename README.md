# netatalk.io

Netatalk static website.

The core website is generated from Markdown sources using Python scripts in `scripts/`,
orchestrated by the `build.sh` shell script.

Release notes as well as wiki documentation sources are fetched remotely
from the Netatalk/netatalk GitHub project by the build script,
and not kept under revision control in this repository.

The Markdown sources of `manual/` as well as html pages in `public/developer/`
should not be modified directly, but rather synced from Netatalk/netatalk for each release.
See the [Netatalk release process](https://github.com/Netatalk/netatalk/wiki/Release-Process)
for how to refresh these sources.

## New release procedure

- Refresh the sources in `manual` and `public/developer` as described above.
- Create a news story at the top of `archive.md` (the top three stories will be substituted to `index.md`.)
- Prepend the release version to the VERSIONS list in `scripts/common.py`.
- Run the `build.sh` script, passing a GITHUB_TOKEN env variable with a valid GitHub API token.
- Commit all above changes and push to remote git to publish to web hosting.

When introducing a new *minor* release series, you also need to create a new public subdir with a `.gitkeep` file,
e.g. `public/4.4/.gitkeep`.

When introducing a new *major* release series, update `scripts/generate_homepage.py` and `documentation.md`
to iterate over the new release versions (e.g. *4.\**) and substitute a list of release notes,
e.g. `NETATALK_V4_RELEASE_NOTES`.
