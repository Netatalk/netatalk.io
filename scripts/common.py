import os
import re
import tomllib
from functools import lru_cache
from pathlib import Path
from string import Template
from urllib.parse import urljoin

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "config"
TEMPLATES = ROOT / "templates"
NETATALK_MESON_BUILD = ROOT / "netatalk" / "meson.build"
RELEASES_FILE = CONFIG / "releases.txt"
SITE_CONFIG_FILE = CONFIG / "site.toml"

with SITE_CONFIG_FILE.open("rb") as config_file:
    SITE_CONFIG = tomllib.load(config_file)

LOCALES = SITE_CONFIG["locales"]
DEFAULT_SITE_BASE_URL = SITE_CONFIG["base_url"]
SITE_BASE_URL = os.environ.get("NETATALK_SITE_BASE_URL", DEFAULT_SITE_BASE_URL).rstrip("/") + "/"


def site_url(path=""):
    return urljoin(SITE_BASE_URL, str(path).lstrip("/"))


INTERNAL_SITE_URL_PATTERN = re.compile(r"https://netatalk\.io(?:/([^\"'<>\s]*))?")


def localize_internal_site_urls(html):
    return INTERNAL_SITE_URL_PATTERN.sub(
        lambda match: site_url(match.group(1) or ""),
        html,
    )


def load_versions():
    versions = [
        line.strip()
        for line in RELEASES_FILE.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    ]

    if len(versions) != len(set(versions)):
        raise RuntimeError(f"Duplicate versions in {RELEASES_FILE}")

    return versions


VERSIONS = load_versions()


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
