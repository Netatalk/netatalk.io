# netatalk.io

Netatalk static website.

The entire site is generated from Markdown sources using custom Python scripts.

Release notes as well as wiki documentation sources are fetched remotely from the Netatalk/netatalk GitHub project.

The contents of `manual/` should not be modified directly, but rather synced from Netatalk/netatalk for each release.
See the [Netatalk release process](https://github.com/Netatalk/netatalk/wiki/Release-Process) for how to refresh these sources.

## New release procedure

- Create a news story at the top of `index.md`.
- Move an older news story to `archive.md`. Limit the number of news stories on `index.md` to 4 or less.
- Add link to release notes in `documentation.md`.
- Prepend release version to VERSIONS in `scripts/common.py`
- Run the `build.sh` script, passing a GITHUB_TOKEN env variable with a valid GitHub API token.
- Validate the correctness (and absence of spam for wiki) in generated html sources in `public/`.
- Refresh the manual pages as described in the previous section.
- Commit all above changes and push to remote git.
- The web host (currently: CloudFlare) will automatically build and publish the site via a webhook trigger.
