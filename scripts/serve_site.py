#!/usr/bin/env python3
import argparse
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


class ExtensionFallbackHandler(SimpleHTTPRequestHandler):
    def translate_path(self, path):
        translated = Path(super().translate_path(path))
        if translated.exists() or translated.suffix:
            return str(translated)

        html_path = translated.with_suffix(".html")
        if html_path.is_file():
            return str(html_path)

        return str(translated)


def main():
    parser = argparse.ArgumentParser(description="Serve the generated Netatalk website.")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", default=8000, type=int)
    parser.add_argument("--directory", default="public")
    args = parser.parse_args()

    handler = lambda *handler_args, **handler_kwargs: ExtensionFallbackHandler(
        *handler_args,
        directory=args.directory,
        **handler_kwargs,
    )
    server = ThreadingHTTPServer((args.host, args.port), handler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
