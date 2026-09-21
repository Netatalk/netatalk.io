"""Build the Pagefind search indexes.

Pages marked data-pagefind-body form the main index. Developer content
(Doxygen output and developer wiki pages, marked data-search-tier) forms a
second index that the search UI merges in at a lower weight.
"""
import subprocess
import sys

from common import DEVELOPER_SEARCH_GLOBS, ROOT

PUBLIC = ROOT / "public"
DEVELOPER_TAG = ' data-search-tier="developer"'


def tag_doxygen_pages():
    for page in (PUBLIC / "developer").glob("*.html"):
        html = page.read_text(encoding="utf-8", errors="surrogateescape")
        tagged = html.replace('<div id="doc-content">', f'<div id="doc-content"{DEVELOPER_TAG}>', 1)
        if tagged != html:
            page.write_text(tagged, encoding="utf-8", errors="surrogateescape")


def pagefind(*args):
    subprocess.run([sys.executable, "-m", "pagefind", "--site", str(PUBLIC), *args], check=True)


tag_doxygen_pages()
pagefind()
pagefind(
    "--glob", "{" + ",".join(DEVELOPER_SEARCH_GLOBS) + "}",
    "--root-selector", "[data-search-tier]",
    "--force-language", "en",
    "--output-path", str(PUBLIC / "developer" / "pagefind"),
)
