# netatalk-homepage
Netatalk static website.

The first layer of index pages are generated from fragments of static html.

Release notes as well as wiki documentation pages are static html generated from markdown sources hosted on GitHub. See the Python scripts in the wiki/ dir.

Manual pages are static html generated with xsltproc from [XSL sources](https://github.com/Netatalk/netatalk/tree/main/doc).

# New release procedure
- Create a news story at the top of `index.html.in`.
- Move an older news story to `archive.html.in`. Limit the number of news stories on `index.html.in` to about 4.
- Update the current releases left rail in the `header.html.in` sources.
- Update `download.html.in` and `documentation.html.in` sources.
- Add the new netatalk release version to the "versions" list in `scripts/generate_releasenotes.py`
- Run the `run.sh` script, passing a GITHUB_TOKEN env variable with a valid GitHub API token.
- Validate the correctness and absence of spam in generated html sources in `public/`, then push to remote git.

# See also
- [Netatalk release process wiki](https://github.com/Netatalk/netatalk/wiki/Developer-Notes#user-content-Making_a_release)
