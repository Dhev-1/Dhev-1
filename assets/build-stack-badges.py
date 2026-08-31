#!/usr/bin/env python3
"""Generate the labelled shields.io rows in the Technology Stack section.

The rows are deliberately NOT themed to the page palette: forcing every logo to
one colour flattens the marks into grey noise. Brand colours are what makes a
badge wall read as a badge wall, so we let shields use each icon's own colour
and keep only the pill dark.

A few marks are gone from Simple Icons, so shields renders an empty logo slot
for them. Where an older release still ships the glyph we inline it as a
data URI (see build-fallback-logos.py); where the URL that produces would blow
past what GitHub's camo proxy accepts, the badge stays text-only.

Rewrites everything between the stack markers in README.md.

Run:  python3 assets/build-stack-badges.py
"""

import base64
import pathlib
import re
import sys
import urllib.parse
import urllib.request

PILL = "161B22"        # a touch lighter than GitHub's dark canvas, so pills read
GOLD = "D9B87C"        # the page accent, used only on the category labels
PIN = "https://cdn.jsdelivr.net/npm/simple-icons@11/icons"

BEGIN = "<!-- stack:begin -->"
END = "<!-- stack:end -->"

# Marks Simple Icons has dropped; value is the brand colour to bake into the
# inlined glyph, since shields will not recolour a data URI.
INLINE = {"playwright": "#2EAD33"}

# label -> Simple Icons slug. None means text-only: either no glyph exists
# anywhere (Karma, C#, most of the Rust and Wayland tooling) or the glyph is too
# path-heavy to inline without tripping camo's URL limit (AWS S3 answers 414).
ROWS = [
    ("Programming", [
        ("Rust", "rust"), ("Python", "python"), ("TypeScript", "typescript"),
        ("JavaScript", "javascript"), ("C++", "cplusplus"), ("C#", None),
        ("Kotlin", "kotlin"), ("Dart", "dart"), ("QML", "qt"), ("Bash", "gnubash"),
    ]),
    ("Frontend & UI", [
        ("React", "react"), ("Angular", "angular"), ("Astro", "astro"),
        ("Tailwind CSS", "tailwindcss"), ("Vite", "vite"), ("Material UI", "mui"),
        ("Flutter", "flutter"), ("Jetpack Compose", "jetpackcompose"),
        ("GSAP", "greensock"), ("Lenis", None),
    ]),
    ("Backend & APIs", [
        ("Node.js", "nodedotjs"), ("Express", "express"), ("NestJS", "nestjs"),
        ("FastAPI", "fastapi"), ("ASP.NET Core", "dotnet"),
        ("Socket.IO", "socketdotio"), ("Pydantic", "pydantic"),
        ("Uvicorn", None), ("JWT", "jsonwebtokens"), ("Passport", "passport"),
    ]),
    ("Data & Storage", [
        ("PostgreSQL", "postgresql"), ("Prisma", "prisma"), ("SQLite", "sqlite"),
        ("Firebase", "firebase"), ("Firestore", "firebase"),
        ("AWS S3", None), ("SQLx", None),
    ]),
    ("Distributed & AI", [
        ("Temporal", "temporal"), ("LangChain", "langchain"), ("LangGraph", None),
        ("OpenTelemetry", "opentelemetry"), ("MCP", None), ("Zod", "zod"),
    ]),
    ("Testing & Rigor", [
        ("pytest", "pytest"), ("Jest", "jest"), ("Vitest", "vitest"),
        ("Playwright", "playwright"), ("insta", None), ("Karma", None),
        ("supertest", None),
    ]),
    ("Infrastructure", [
        ("Docker", "docker"), ("GitHub Actions", "githubactions"), ("Git", "git"),
        ("GitHub", "github"), ("Gradle", "gradle"),
        ("Android Studio", "androidstudio"),
    ]),
    ("Linux & Systems", [
        ("Arch Linux", "archlinux"), ("Hyprland", "hyprland"),
        ("Wayland", "wayland"), ("Quickshell", "qt"), ("SDDM", None),
        ("kitty", None), ("Zsh", "zsh"), ("Neovim", "neovim"), ("swww", None),
    ]),
]

_cache = {}


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "profile-readme-build"})
    with urllib.request.urlopen(req, timeout=20) as r:
        return r.read().decode()


def inline_logo(slug, colour):
    """Fetch a dropped glyph from a pinned release and bake the brand colour in."""
    if slug not in _cache:
        svg = get(f"{PIN}/{slug}.svg").replace("<svg ", f'<svg fill="{colour}" ', 1)
        b64 = base64.b64encode(svg.encode()).decode()
        _cache[slug] = "data:image/svg%2Bxml;base64," + urllib.parse.quote(b64, safe="")
    return _cache[slug]


def badge(label, slug):
    text = urllib.parse.quote(label.replace("-", "--").replace("_", "__"))
    url = f"https://img.shields.io/badge/{text}-{PILL}?style=flat-square"
    if slug in INLINE:
        url += "&logo=" + inline_logo(slug, INLINE[slug])
    elif slug:
        url += f"&logo={slug}"          # no logoColor: shields uses the brand colour
    alt = label.replace("&", "&amp;").replace("<", "&lt;")
    return f'<img src="{url}" alt="{alt}"/>'


def label_badge(group):
    """The category name as a gold pill - the one place the page palette shows."""
    text = urllib.parse.quote(group.upper().replace("-", "--").replace("_", "__"))
    url = (f"https://img.shields.io/badge/{text}-{GOLD}"
           f"?style=flat-square&labelColor={GOLD}")
    alt = group.replace("&", "&amp;")
    return f'<img src="{url}" alt="{alt}"/>'


def main():
    # No <table>: GitHub draws a 1px border on every cell, which turns the wall
    # into a spreadsheet. Each group is its own centred paragraph led by a gold
    # label pill, so the section reads as badges rather than as a grid.
    groups = []
    for group, items in ROWS:
        badges = " ".join(badge(l, s) for l, s in items)
        groups.append(label_badge(group) + " " + badges)
    block = "\n\n".join(groups)

    path = pathlib.Path(__file__).resolve().parent.parent / "README.md"
    src = path.read_text()
    if BEGIN not in src or END not in src:
        print(f"markers {BEGIN} / {END} not found in {path}", file=sys.stderr)
        return 1
    out = re.sub(re.escape(BEGIN) + r".*?" + re.escape(END),
                 f"{BEGIN}\n{block}\n{END}", src, flags=re.S)
    path.write_text(out)
    print(f"wrote {sum(len(i) for _, i in ROWS)} badges in {len(ROWS)} rows -> {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
