#!/usr/bin/env bash
set -ex
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
git submodule update --init --recursive netatalk
(
  cd netatalk
  docs_install_path="$(pwd)/.."
  meson_setup_args=(
    build
    --prefix "$docs_install_path"
    --localstatedir "$docs_install_path/var"
    --sharedstatedir "$docs_install_path/var/lib"
    -Dwith-appletalk=true
    -Dwith-website=true
    -Dwith-docs-l10n=true
    -Dwith-docs-install-path="$docs_install_path"
    -Dwith-docs-only=true
  )
  if [ -d build/meson-info ]; then
    meson setup --reconfigure "${meson_setup_args[@]}"
  else
    meson setup "${meson_setup_args[@]}"
  fi
  meson compile -C build
  meson install -C build
)
rm -rf wiki
git clone https://github.com/Netatalk/netatalk.wiki.git wiki

python3 scripts/generate_manual.py
python3 scripts/generate_wiki.py
python3 scripts/generate_releasenotes.py
python3 scripts/generate_homepage.py

rm -rf wiki
