import os
import re
import markdown
from markdown.extensions.toc import TocExtension

from common import (
    VERSION,
    LOCALES,
    localize_internal_site_urls,
    render_page,
    toc_sidebar,
)


OPTION_PARAGRAPH = re.compile(
    r'<p>(?P<name>[a-z0-9][a-z0-9 _-]*[a-z0-9]) = (?P<syntax>(?:(?!</p>).)*?<strong>\([GVH]\)</strong>)</p>',
    re.DOTALL,
)


def option_headings(html):
    """Turn "name = value **(G)**" option paragraphs into linkable headings.

    Each option gets an anchor named after it and a high search weight, so
    searches for an option land on its definition.
    """
    seen = {}

    def replace(match):
        name = match.group("name")
        slug = re.sub(r"[^a-z0-9]+", "-", name)
        seen[slug] = seen.get(slug, 0) + 1
        if seen[slug] > 1:
            slug = f"{slug}-{seen[slug]}"
        syntax = " ".join(match.group("syntax").split())
        return (
            f'<h3 class="option" id="{slug}" data-pagefind-weight="10">'
            f'<a class="toclink" href="#{slug}">{name}</a> '
            f'<span class="option-syntax">= {syntax}</span></h3>'
        )

    return OPTION_PARAGRAPH.sub(replace, html)


# Generate manual

for lang in LOCALES:
    navbar = ""
    files = []
    with open(f"./manual/{lang}/_Sidebar.md", "r", encoding="utf-8") as input_file:
        text = input_file.read()
        # The sidebar source in the netatalk repo opens with its own
        # locale switcher; the site renders one in the search box instead.
        text = re.sub(r"^\[en\]\([^)]*\)\s*\|\s*\[ja\]\([^)]*\)\s*\n", "", text)
        html = markdown.markdown(
            text,
            extensions=[
                'fenced_code',
                'smarty',
                'tables',
            ],
            output_format='html',
        )
        html = localize_internal_site_urls(html)

        navbar = toc_sidebar(html)

    for file in os.listdir(f"./manual/{lang}/"):
        if file.endswith(".md"):
            files.append(f"{file}")
    for file in files:
        if file == "_Sidebar.md":
            continue
        with open(f"./manual/{lang}/{file}", "r", encoding="utf-8") as input_file:
            text = input_file.read()
            text = re.sub(
                r'(?m)^([ \t]{0,3}#(?!#)[ \t]+[^\r\n]+)',
                r'\1\n\n[TOC]\n\n',
                text,
                count=1,
            )
            html = markdown.markdown(
                text,
                extensions=[
                    'fenced_code',
                    'smarty',
                    'tables',
                    TocExtension(
                        anchorlink=True,
                    ),
                ],
                output_format='html',
            )
            html = option_headings(localize_internal_site_urls(html))
        page_title = file.replace('index', 'Index').replace('.md', '')
        new_name = file.replace('.md', '.html')

        with open(f"./public/manual/{lang}/{new_name}", "w", encoding="utf-8", errors="xmlcharrefreplace") as output_file:
            output_file.write(render_page(
                f"Netatalk Manual - {page_title}",
                f"manual/{lang}/{new_name}",
                html,
                lang=lang,
                sidebar=navbar,
            ))

        print(f"Converted: {lang}/{file}")


# Generate READMEs

files = []

for file in os.listdir("./manual/"):
    if file.endswith(".md"):
        files.append(f"{file}")
for file in files:
    with open(f"./manual/{file}", "r", encoding="utf-8") as input_file:
        text = input_file.read()
        text = re.sub(r"\s<[^<>]+@[a-zA-Z0-9._-]+>", "", text)
        html = markdown.markdown(
            text,
            extensions=[
                'fenced_code',
                'smarty',
                'tables',
            ],
            output_format='html',
        )
        html = localize_internal_site_urls(html)
    new_name = file.replace('.md', '.html').lower()
    h1_match = re.search(r'^# (.+)$', text, re.MULTILINE)
    if h1_match:
        page_title = h1_match.group(1)
    else:
        page_title = file.replace('.md', '').replace('_', ' ').capitalize()

    with open(f"./public/{new_name}", "w", encoding="utf-8", errors="xmlcharrefreplace") as output_file:
        output_file.write(render_page(f"Netatalk - {page_title}", new_name, html))

    print(f"Converted: {new_name}")


# Generate Netatalk Client manual

client_manual_dir = "./client/manual/en"
client_output_dir = "./public/client/manual/en"
os.makedirs(client_output_dir, exist_ok=True)

with open(f"{client_manual_dir}/_Sidebar.md", "r", encoding="utf-8") as input_file:
    html = markdown.markdown(
        input_file.read(),
        extensions=[
            'fenced_code',
            'smarty',
            'tables',
        ],
        output_format='html',
    )
    navbar = toc_sidebar(localize_internal_site_urls(html))

for file in sorted(os.listdir(client_manual_dir)):
    if not file.endswith(".md") or file == "_Sidebar.md":
        continue

    with open(f"{client_manual_dir}/{file}", "r", encoding="utf-8") as input_file:
        text = input_file.read()
        text = re.sub(
            r'(?m)^([ \t]{0,3}#(?!#)[ \t]+[^\r\n]+)',
            r'\1\n\n[TOC]\n\n',
            text,
            count=1,
        )
        html = markdown.markdown(
            text,
            extensions=[
                'fenced_code',
                'smarty',
                'tables',
                TocExtension(
                    anchorlink=True,
                ),
            ],
            output_format='html',
        )
        html = localize_internal_site_urls(html)

    page_title = file.replace('index', 'Index').replace('.md', '')
    new_name = file.replace('.md', '.html')
    output_path = f"client/manual/en/{new_name}"

    with open(f"{client_output_dir}/{new_name}", "w", encoding="utf-8", errors="xmlcharrefreplace") as output_file:
        output_file.write(render_page(
            f"Netatalk Client Manual - {page_title}",
            output_path,
            html,
            sidebar=navbar,
        ))

    print(f"Converted: {output_path}")
