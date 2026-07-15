import re
import os
from functools import lru_cache
from pathlib import Path
from string import Template
from urllib.parse import urljoin

LOCALES = ["en", "ja"]
ROOT = Path(__file__).resolve().parents[1]
TEMPLATES = ROOT / "templates"
NETATALK_MESON_BUILD = ROOT / "netatalk" / "meson.build"
DEFAULT_SITE_BASE_URL = "https://netatalk.io/"
SITE_BASE_URL = os.environ.get("NETATALK_SITE_BASE_URL", DEFAULT_SITE_BASE_URL).rstrip("/") + "/"


def site_url(path=""):
    return urljoin(SITE_BASE_URL, str(path).lstrip("/"))


INTERNAL_SITE_URL_PATTERN = re.compile(r"https://netatalk\.io(?:/([^\"'<>\s]*))?")


def localize_internal_site_urls(html):
    return INTERNAL_SITE_URL_PATTERN.sub(
        lambda match: site_url(match.group(1) or ""),
        html,
    )


# List of Netatalk releases 2023 onwards, which have release notes on GitHub.
# Earlier release notes are revision controlled in this repository.
VERSIONS = [
    "4.5.0",
    "4.5.0beta",
    "4.4.3",
    "4.4.2",
    "4.4.1",
    "4.4.0",
    "4.3.2",
    "4.3.1",
    "4.3.0",
    "4.2.4",
    "4.2.3",
    "4.2.2",
    "4.2.1",
    "4.2.0",
    "4.1.2",
    "4.1.1",
    "4.1.0",
    "4.0.8",
    "4.0.7",
    "4.0.6",
    "4.0.5",
    "4.0.4",
    "4.0.3",
    "4.0.2",
    "4.0.1",
    "4.0.0",
    "3.2.10",
    "3.2.9",
    "3.2.8",
    "3.2.7",
    "3.2.6",
    "3.2.5",
    "3.2.4",
    "3.2.3",
    "3.2.2",
    "3.2.1",
    "3.2.0",
    "3.1.19",
    "3.1.18",
    "3.1.17",
    "3.1.16",
    "3.1.15",
    "3.1.14",
    "2.4.10",
    "2.4.9",
    "2.4.8",
    "2.4.7",
    "2.4.6",
    "2.4.5",
    "2.4.4",
    "2.4.3",
    "2.4.2",
    "2.4.1",
    "2.4.0",
    "2.3.2",
    "2.3.1",
    "2.3.0",
    "2.2.10",
    "2.2.9",
    "2.2.8",
    "2.2.7",
]

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


def html_head(title, path, lang="en"):
    return render_template(
        "document-head.html",
        canonical_url=site_url(path),
        lang=lang,
        site_base_url=SITE_BASE_URL,
        title=title,
    )


def html_menlinks():
    return render_template("site-header.html", site_base_url=SITE_BASE_URL)


def html_navbar(version):
    minor_version = re.search(r"^(\d+\.\d+)", version).group()
    dashed_version = version.replace(".", "-")
    return render_template(
        "site-navigation.html",
        dashed_version=dashed_version,
        minor_version=minor_version,
        site_base_url=SITE_BASE_URL,
        version=version,
    )


def html_foot(path):
    return render_template(
        "site-footer.html",
        page_url=site_url(path),
        site_base_url=SITE_BASE_URL,
    )


def js_mermaid():
    return render_template("mermaid-scripts.html")
