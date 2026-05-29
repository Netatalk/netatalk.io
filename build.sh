#!/usr/bin/env bash
set -ex
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
for tool in cc git meson ninja doxygen po4a pandoc; do
  if ! command -v "$tool" >/dev/null 2>&1; then
    echo "Missing required build tool: $tool" >&2
    exit 1
  fi
done
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
    -Dwith-docs-l10n=true
    -Dwith-docs-install-path="$docs_install_path"
    -Dwith-docs-only=true
    -Dwith-testsuite=true
    -Dwith-website=true
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
