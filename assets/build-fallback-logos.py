#!/usr/bin/env python3
"""Emit shields.io badge markup for logos shields no longer carries.

Simple Icons has dropped a handful of marks (LinkedIn, Playwright, AWS S3 among
them), so `&logo=<slug>` silently renders a badge with an empty logo slot.
simple-icons@11 on jsdelivr still ships the glyphs, so we fetch them, bake the
accent colour in (shields does not recolour a data-URI logo) and hand back a
ready-to-paste data URI.

Two marks stay text-only: Karma has no glyph in any version, and the AWS S3
glyph is so path-heavy that its data URI pushes the badge URL past the length
GitHub's camo proxy accepts (it answers 414 and the image never loads). Keep an
eye on that ceiling: Playwright, at ~1.5 kB, proxies fine.

Run:  python3 assets/build-fallback-logos.py
"""

import base64
import sys
import urllib.parse
import urllib.request

GOLD, FELT, BONE = "#D9B87C", "#2E7D5B", "#E8E3DA"
BG = "0B0B0D"
PIN = "https://cdn.jsdelivr.net/npm/simple-icons@11/icons"

# label -> (simple-icons slug, accent for the row it sits in)
WANTED = {
    "LinkedIn":   ("linkedin", GOLD),
    "Playwright": ("playwright", BONE),
}


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "profile-readme-build"})
    with urllib.request.urlopen(req, timeout=20) as r:
        return r.read().decode()


def data_uri(slug, colour):
    svg = get(f"{PIN}/{slug}.svg")
    if "<svg " not in svg:
        raise ValueError("not an svg")
    svg = svg.replace("<svg ", f'<svg fill="{colour}" ', 1)
    b64 = base64.b64encode(svg.encode()).decode()
    return "data:image/svg%2Bxml;base64," + urllib.parse.quote(b64, safe="")


def main():
    for label, (slug, colour) in WANTED.items():
        uri = data_uri(slug, colour)
        badge = (f"https://img.shields.io/badge/{urllib.parse.quote(label)}-{BG}"
                 f"?style=flat-square&labelColor={BG}&logo={uri}")
        print(f'<img src="{badge}" alt="{label}"/>\n')
    return 0


if __name__ == "__main__":
    sys.exit(main())
