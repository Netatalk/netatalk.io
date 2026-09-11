# Netatalk Logo

This directory contains the canonical Netatalk logo images.

## Current logo

| File | Contents | Size |
|------|----------|------|
| `logo.svg` / `logo.png` | Full lockup: the mark beside the Netatalk wordmark on a navy tile | 826 × 240 viewBox; PNG 3304 × 960 |
| `logo-mark.svg` / `logo-mark.png` | The square mark alone, for avatars, app icons and other places where only an icon fits | 512 × 512 viewBox; PNG 1024 × 1024 |

The mark is two interlocking chain links: a secure, unbreakable connection between two endpoints.
The palette is navy `#0B1F3A` for the tile, electric blue `#3D82FF` and cyan `#19E3D2`,
with the blue-to-cyan gradient running across the second link and again across the wordmark.

The wordmark is set in [Comfortaa](https://fonts.google.com/specimen/Comfortaa) at weight 700
(SIL Open Font License 1.1), converted to outlines with an added rounded stroke so the letter
weight matches the mark. The SVG files therefore carry no font dependency.

The PNG files are rendered from the SVG files with `rsvg-convert`; the SVG is the source of truth.
The website banner uses the same lockup artwork from `gfx/logo-lockup.svg`.

The logo was created in 2026 for the website redesign and is distributed under the GNU GPL 2.0,
like the rest of this repository.

## Legacy logo (2005)

`logo.ai` and `logo.pdf` are the vector sources of the previous logo, the Netatalk daemon roundel.
It continues to appear on the website as the footer mascot (`gfx/daemon-*.png`).

The logo was first published on January 4th 2005 on the cover page for the first edition of the
[Netatalk manual PDF](https://netatalk.io/2.0/Netatalk-Manual.pdf) created by Thomas Kaiser.
The manual is distributed under the GNU GPL 2.0,
so the logo image is assumed to be distributed under the same license.

[The original artist is unknown](https://sourceforge.net/p/netatalk/mailman/message/22681994/).
However, the images were [redrawn from scratch by Tim Lindner](https://github.com/Netatalk/netatalk-doc/commit/391711d12b2333712cedfbc4da0e55971b06837d)
as vector graphics in PDF and Illustrator formats, and committed to version control on June 6th 2009.
