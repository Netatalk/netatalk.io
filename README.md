# netatalk-homepage

Netatalk html website.

The entire site, save for historical manual pages, is generated from Markdown sources.

Release notes as well as wiki documentation pages are generated from Markdown sources from GitHub release notes and wiki on the fly.

The contents of `manual/` should not be modified directly, but rather built from netatalk sources and installed into this location.
See the [Netatalk release process](https://github.com/Netatalk/netatalk/wiki/Release-Process) for the detailed procedure.

# New release procedure
- Create a news story at the top of `index.md`.
- Move an older news story to `archive.md`. Limit the number of news stories on `index.md` to about 4.
- Add link to release notes in `documentation.md`.
- Append release version to VERSIONS in `scripts/common.py`
- Run the `build.sh` script, passing a GITHUB_TOKEN env variable with a valid GitHub API token.
- Validate the correctness (and absence of spam for wiki) in generated html sources in `public/`.
- Commit all above changes and push to remote git.
- The web host (currently: CloudFlare) will automatically build and publish the site via a webhook trigger.
