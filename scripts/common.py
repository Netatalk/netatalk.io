import fnmatch
import os
import re
import tomllib
from functools import lru_cache
from pathlib import Path
from string import Template
from urllib.parse import urljoin, urlsplit

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "config"
TEMPLATES = ROOT / "templates"
NETATALK_MESON_BUILD = ROOT / "netatalk" / "meson.build"
RELEASES_FILE = CONFIG / "releases.txt"
CLIENT_RELEASES_FILE = CONFIG / "client-releases.txt"
SITE_CONFIG_FILE = CONFIG / "site.toml"

with SITE_CONFIG_FILE.open("rb") as config_file:
    SITE_CONFIG = tomllib.load(config_file)

LOCALES = SITE_CONFIG["locales"]
DEFAULT_SITE_BASE_URL = SITE_CONFIG["base_url"]
SITE_BASE_URL = os.environ.get("NETATALK_SITE_BASE_URL", DEFAULT_SITE_BASE_URL).rstrip("/") + "/"
# Root-relative links follow the browser's current origin, including preview
# deployment URLs. Retain the configured path for sites hosted in a subdirectory.
INTERNAL_SITE_BASE_URL = urlsplit(SITE_BASE_URL).path or "/"

DEVELOPER_SEARCH_GLOBS = (
    "developer/*.html",
    "docs/Dev-Docs*.html",
    "docs/Developer-*.html",
    "docs/Using-*.html",
    "docs/Benchmarks.html",
    "docs/CatalogSearch.html",
    "docs/DirCache-redundant-stat-ops.html",
    "docs/Release-Process.html",
    "docs/Roadmap.html",
    "docs/Testing.html",
    "docs/Work-with-Documentation.html",
    "client/developer.html",
)

LOW_PRIORITY_SEARCH_WEIGHT = "0.3"


def site_url(path=""):
    """Return an internal URL that uses the browser's current origin."""
    return urljoin(INTERNAL_SITE_BASE_URL, str(path).lstrip("/"))


def absolute_site_url(path=""):
    """Return an absolute URL for canonical tags, sitemaps, and validators."""
    return urljoin(SITE_BASE_URL, str(path).lstrip("/"))


INTERNAL_SITE_URL_PATTERN = re.compile(
    r"https://netatalk\.io(?=/|[?#\"'<>\s]|$)([^\"'<>\s]*)"
)


def localize_internal_site_urls(html):
    return INTERNAL_SITE_URL_PATTERN.sub(
        lambda match: site_url(match.group(1) or ""),
        html,
    )


def load_versions(releases_file=RELEASES_FILE):
    versions = [
        line.strip()
        for line in releases_file.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    ]

    if len(versions) != len(set(versions)):
        raise RuntimeError(f"Duplicate versions in {releases_file}")

    return versions


VERSIONS = load_versions()
CLIENT_VERSIONS = load_versions(CLIENT_RELEASES_FILE)
CLIENT_VERSION = CLIENT_VERSIONS[0]


def netatalk_version():
    meson_build = NETATALK_MESON_BUILD.read_text(encoding="utf-8")
    match = re.search(r"^\s*version:\s*['\"]([^'\"]+)['\"]", meson_build, re.MULTILINE)
    if match is None:
        raise RuntimeError(f"Unable to find project version in {NETATALK_MESON_BUILD}")
    return match.group(1)


VERSION = netatalk_version()


@lru_cache
def load_template(name):
    return Template((TEMPLATES / name).read_text(encoding="utf-8"))


def render_template(name, **context):
    return load_template(name).substitute(context)


@lru_cache
def css_hash():
    """Content hash of the stylesheet, used to cache-bust its URL."""
    import hashlib

    css = (ROOT / "css" / "site.css").read_bytes()
    return hashlib.sha256(css).hexdigest()[:10]


def html_head(title, path, lang="en"):
    return render_template(
        "document-head.html",
        canonical_url=absolute_site_url(path),
        css_hash=css_hash(),
        lang=lang,
        site_base_url=INTERNAL_SITE_BASE_URL,
        title=title,
    )


def html_menlinks():
    return render_template("site-header.html", site_base_url=INTERNAL_SITE_BASE_URL)


def html_navbar(version):
    minor_version = re.search(r"^(\d+\.\d+)", version).group()
    dashed_version = version.replace(".", "-")
    client_minor_version = re.search(r"^(\d+\.\d+)", CLIENT_VERSION).group()
    return render_template(
        "site-navigation.html",
        client_minor_version=client_minor_version,
        client_version=CLIENT_VERSION,
        dashed_version=dashed_version,
        minor_version=minor_version,
        site_base_url=INTERNAL_SITE_BASE_URL,
        version=version,
    )


def lang_switcher(path, lang):
    """en | ja switcher for the search box.

    Manual pages link to their counterpart in the other locale; other
    pages link into the manual root of the other language. The page's
    language also selects Pagefind's search index, so this switches
    both the content and the search language.
    """
    match = re.match(r"manual/(\w+)/(.*)$", str(path).lstrip("/"))
    links = []
    for locale in LOCALES:
        if locale == lang:
            links.append(f'<span aria-current="true">{locale}</span>')
        elif match:
            links.append(f'<a href="{site_url(f"manual/{locale}/{match.group(2)}")}">{locale}</a>')
        else:
            links.append(f'<a href="{site_url(f"manual/{locale}/")}">{locale}</a>')
    return " | ".join(links)


def html_search(path="", lang="en"):
    return render_template(
        "site-search.html",
        lang_switcher=lang_switcher(path, lang),
        site_base_url=INTERNAL_SITE_BASE_URL,
    )


def html_foot(path):
    return render_template(
        "site-footer.html",
        page_url=absolute_site_url(path),
        site_base_url=INTERNAL_SITE_BASE_URL,
    )


def js_mermaid():
    return render_template("mermaid-scripts.html")


def toc_sidebar(inner_html):
    """Wrap rendered sidebar HTML in the standard table-of-contents section."""
    return f"""<section class="navbar" aria-label="Table of contents">
<h2>Table of contents</h2>
{inner_html}
</section>
"""


def is_developer_page(path):
    """Pages written for Netatalk developers rather than administrators."""
    clean = str(path).lstrip("/")
    return any(fnmatch.fnmatchcase(clean, glob) for glob in DEVELOPER_SEARCH_GLOBS)


def search_body_attributes(path):
    """Attributes on <main> that place the page in the site search.

    Developer pages are indexed separately at a lower weight (see
    build_search_index.py). Release notes and the news pages are indexed
    at reduced weight so the manual and man pages outrank them.
    """
    if is_developer_page(path):
        return ' data-search-tier="developer"'
    clean = str(path).lstrip("/")
    if re.match(r"(client/)?\d+\.\d+/", clean) or clean in ("news.html", "archive.html"):
        return f' data-pagefind-body data-pagefind-weight="{LOW_PRIORITY_SEARCH_WEIGHT}"'
    return " data-pagefind-body"


def mark_current_page(html, path):
    """Add aria-current to links that point at the page being rendered.

    Links are either absolute site URLs (main navigation) or relative to
    the page's directory (manual/wiki tables of contents). Matches the
    href regardless of any attributes that follow it.
    """
    url = site_url(path)
    basename = str(path).rstrip("/").rsplit("/", 1)[-1]
    candidates = {url, basename}
    if basename == "index.html":
        candidates.add(url[: -len("index.html")])
    pattern = re.compile(
        r'(<a\b[^>]*?)href="({})"'.format("|".join(re.escape(c) for c in candidates))
    )
    return pattern.sub(r'\1href="\2" aria-current="page"', html)


def render_page(title, path, content, *, lang="en", sidebar=None, mermaid=False):
    """Assemble a complete page: head, header, main content, sidebar, footer.

    `sidebar` is the aside's inner HTML placed after the search box;
    defaults to the standard site navigation. `content` is the main
    element's inner HTML.
    """
    if sidebar is None:
        sidebar = html_navbar(VERSION)
    sidebar = mark_current_page(html_search(path, lang) + sidebar, path)

    parts = [
        html_head(title, path, lang),
        "<body>\n",
        js_mermaid() if mermaid else "",
        mark_current_page(html_menlinks(), path),
        f'<div class="page">\n<main id="content"{search_body_attributes(path)}>\n',
        content,
        '\n</main>\n<aside class="site-aside">\n',
        sidebar,
        "</aside>\n</div>\n",
        html_foot(path),
    ]
    return "".join(parts)
