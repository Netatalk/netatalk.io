#!/usr/bin/env bash
set -euo pipefail

mode="build"
host="127.0.0.1"
port="8000"
base_url="${NETATALK_SITE_BASE_URL:-}"

usage() {
  cat <<EOF
Usage: $0 [test] [--base-url URL] [--host HOST] [--port PORT]

Modes:
  build  Build the static site. This is the default.
  test   Build the static site for localhost and serve ./public.

Options:
  --base-url URL  Base URL for generated internal URLs.
  --host HOST     Host to bind in test mode. Default: 127.0.0.1
  --port PORT     Port to bind in test mode. Default: 8000
EOF
}

require_arg() {
  if [ "$#" -lt 2 ]; then
    echo "Missing value for $1" >&2
    usage >&2
    exit 1
  fi
}

while [ "$#" -gt 0 ]; do
  case "$1" in
    build|test)
      mode="$1"
      shift
      ;;
    --test)
      mode="test"
      shift
      ;;
    --base-url)
      require_arg "$@"
      base_url="$2"
      shift 2
      ;;
    --host)
      require_arg "$@"
      host="$2"
      shift 2
      ;;
    --port)
      require_arg "$@"
      port="$2"
      shift 2
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Unknown argument: $1" >&2
      usage >&2
      exit 1
      ;;
  esac
done

if [ "$mode" = "test" ] && [ -z "$base_url" ]; then
  base_url="http://${host}:${port}/"
fi

if [ -n "$base_url" ]; then
  export NETATALK_SITE_BASE_URL="$base_url"
fi

set -x
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

if [ "$mode" = "test" ]; then
  set +x
  echo "Serving site at ${NETATALK_SITE_BASE_URL}"
  echo "Press Ctrl-C to stop the server."
  python3 scripts/serve_site.py --host "$host" --port "$port" --directory public
fi
