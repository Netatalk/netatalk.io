#!/usr/bin/env bash
set -ex
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
rm -rf wiki
git clone https://github.com/Netatalk/netatalk.wiki.git wiki

python3 scripts/generate_manual.py
python3 scripts/generate_wiki.py
python3 scripts/generate_releasenotes.py
python3 scripts/generate_homepage.py

rm -rf wiki
