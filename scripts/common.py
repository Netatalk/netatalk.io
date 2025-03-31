import re

LOCALES = ["en", "ja"]

# Netatalk releases 2023 onward which have release notes on GitHub.
# Earlier versions have static release notes html pages.
VERSIONS = [
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

VERSION = max(VERSIONS)

def html_head(title, path, lang="en"):
    return f"""<!doctype html>
<html lang="{lang}">
<head>
    <meta charset="utf-8">
    <title>{title}</title>
    <meta name="description" content="Netatalk Wiki">
    <link rel="canonical" href="https://netatalk.io/{path}">
    <link rel="stylesheet" type="text/css" href="https://netatalk.io/css/site.css">
    <link rel="icon" type="image/x-icon" href="https://netatalk.io/gfx/favicon.ico">
</head>
"""

def html_menlinks():
    return """<body>
<div id="header">
    <div id="logo"></div>
    <div id="menlinks">
        <a href="/" title="Return to Netatalk home">[main]</a>
        <a href="/docs" title="Netatalk Wiki">[wiki]</a>
        <a href="/documentation.html" title="Netatalk Manual">[documentation]</a>
        <a href="/download.html" title="Download Netatalk">[downloads]</a>
        <a href="/support.html" title="Support">[support]</a>
        <a href="/links.html" title="Netatalk related links">[links]</a>
        <img src="/gfx/end.gif" alt="" width="125" height="7">
    </div>
</div>

<div id="header-print">
    <h1>netatalk.io</h1>
</div>

<div class="search">
    <h2>search netatalk.io</h2>
    <form method="get" action="https://duckduckgo.com/">
        <p>
            <input type="text" name="q" size="10" maxlength="255" value="" title="enter search text">
            <input type="hidden" name="sites" value="netatalk.io">
            <input type="submit" value="Go" title="search netatalk.io">
        </p>
    </form>
    <span class="italic">powered by DuckDuckGo</span>
</div>
"""

def html_navbar(version):
    minor_version = re.search(r"^(\d+\.\d+)", version).group()
    dashed_version = version.replace(".", "-")
    return f"""
<div id="navbars">
  <div class="navbar">
    <h2>current releases</h2>
    <ul>
      <li>
        <a
        title="download {version} xz compressed source code"
        href="https://github.com/Netatalk/netatalk/releases/download/netatalk-{dashed_version}/netatalk-{version}.tar.xz">
        Netatalk {version} (source code)
        </a>
      </li>
      <li>
        <a
        title="download {version} checksum"
        href="https://github.com/Netatalk/netatalk/releases/download/netatalk-{dashed_version}/netatalk-{version}.tar.xz.sha256sum">
        Netatalk {version} (sha256sum)
        </a>
      </li>
      <li>
        <a
        title="download {version} Webmin module"
        href="https://github.com/Netatalk/netatalk/releases/download/netatalk-{dashed_version}/netatalk-{version}.wbm.gz">
        Webmin Module
        </a>
      </li>
      <li>
        <a
        title="view {version} Release Notes"
        href="/{minor_version}/ReleaseNotes{version}.html">
        Release Notes
        </a>
      </li>
    </ul>
  </div>
  <div class="navbar">
    <h2>netatalk manual</h2>
    <ol>
      <li><a href="/manual/en/">Introduction</a></li>
      <li><a href="/manual/en/Installation">Installation</a></li>
      <li><a href="/manual/en/Configuration">Configuration</a></li>
      <li><a href="/manual/en/AppleTalk">AppleTalk</a></li>
      <li><a href="/manual/en/Upgrading">Upgrading</a></li>
      <li><a href="/manual/en/Compilation">Compilation</a></li>
    </ol>
  </div>
  <div class="navbar">
    <h2>community</h2>
    <ul>
       <li><a title="Wiki" href="https://github.com/Netatalk/netatalk/wiki">Contribute to Wiki Pages</a></li>
       <li><a title="Discussions" href="https://github.com/Netatalk/netatalk/discussions">Participate in Discussions</a></li>
       <li><a title="Mailing Lists" href="https://sourceforge.net/p/netatalk/mailman/">Subscribe to Mailing Lists</a></li>
    </ul>
  </div>
  <div class="navbar">
    <h2>development</h2>
    <ul>
      <li><a title="Code Repository, GitHub" href="https://github.com/Netatalk/netatalk">Code Repository</a></li>
      <li><a title="Code Repository, GitLab" href="https://gitlab.com/netatalk-team/netatalk">GitLab Mirror</a></li>
      <li><a title="How to Contribute" href="https://netatalk.io/docs/Developer-Notes.html">
        How to Contribute</a></li>
      <li><a title="Static Analysis" href="https://sonarcloud.io/summary/overall?id=Netatalk_netatalk">
        Static Analysis by SonarQube</a></li>
    </ul>
  </div>
  <div class="navbar">
    <h2>continuous integration</h2>
    <p><a href="https://github.com/Netatalk/netatalk/actions/workflows/build.yml">
      <img alt="GitHub Continuous Integration - Build Status" height="22"
         src="https://github.com/Netatalk/netatalk/actions/workflows/build.yml/badge.svg"/>
    </a></p>
    <p><a href="https://github.com/Netatalk/netatalk/actions/workflows/test.yml">
      <img alt="GitHub Continuous Integration - Test Status" height="22"
         src="https://github.com/Netatalk/netatalk/actions/workflows/test.yml/badge.svg"/>
    </a></p>
    <p><a href="https://github.com/Netatalk/netatalk/actions/workflows/containers.yml">
      <img alt="GitHub Continuous Integration - Containers Status" height="22"
         src="https://github.com/Netatalk/netatalk/actions/workflows/containers.yml/badge.svg"/>
    </a></p>
  </div>
</div>
"""

def html_foot(path):
    return f"""
<div class="footer">
    <a href="https://validator.nu/?doc=https://netatalk.io/{path}">
      <img style="border:0;width:88px;height:31px"
      src="https://raw.githubusercontent.com/rdmark/html5-valid-badge/refs/heads/master/html5-validator-badge.svg"
      alt="Valid HTML5">
    </a>
    <a href="https://validator.nu/?doc=https://netatalk.io/{path}">
      <img style="border:0;width:88px;height:31px"
      src="https://www.w3.org/Icons/valid-css-v.svg" alt="Valid CSS">
    </a>
    <p>Netatalk and the Netatalk website are licensed under the <a href="/stable/htmldocs/gpl">GNU
    General Public License 2.0</a>.</p>
</div>
</body>
</html>
"""
