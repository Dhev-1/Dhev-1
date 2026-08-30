#!/usr/bin/env python3
"""Cache Simple Icons glyph paths into assets/icons.json.

The panels draw brand logos monochrome in the page palette rather than pulling
skillicons' multicolour tiles, so the marks stay recognisable without fighting
the design. Run once; the cache is committed so the build works offline.

Run:  python3 assets/fetch-icons.py
"""

import json
import pathlib
import re
import sys
import urllib.request

HERE = pathlib.Path(__file__).parent
OUT = HERE / "icons.json"

# label -> Simple Icons slug. A label with no slug just renders as a text chip.
SLUGS = {
    "Rust": "rust", "Python": "python", "TypeScript": "typescript",
    "C++": "cplusplus", "Kotlin": "kotlin", "C#": "csharp",
    "QML": "qt", "Bash": "gnubash",

    "FastAPI": "fastapi", "NestJS": "nestjs", ".NET Core": "dotnet",
    "Socket.IO": "socketdotio", "PostgreSQL": "postgresql",
    "SQLite": "sqlite", "Prisma": "prisma",

    "React": "react", "Angular": "angular", "Astro": "astro",
    "Compose": "jetpackcompose", "Flutter": "flutter", "GSAP": "greensock",

    "Docker": "docker", "Actions": "githubactions",
    "OTel": "opentelemetry", "pytest": "pytest", "Vitest": "vitest",

    "Arch": "archlinux", "Hyprland": "hyprland", "Wayland": "wayland",
    "Quickshell": "qt", "kitty": "kitty", "Zsh": "zsh", "Neovim": "neovim",
}

PATH_RE = re.compile(r'<path[^>]*\sd="([^"]+)"')


def fetch(slug):
    url = f"https://cdn.simpleicons.org/{slug}"
    req = urllib.request.Request(url, headers={"User-Agent": "profile-readme-build"})
    with urllib.request.urlopen(req, timeout=15) as r:
        body = r.read().decode()
    paths = PATH_RE.findall(body)
    if not paths:
        raise ValueError("no path data")
    # a couple of marks ship as multiple subpaths; concatenating keeps the glyph whole
    return " ".join(paths)


def main():
    cache = json.loads(OUT.read_text()) if OUT.exists() else {}
    missing = []
    for label, slug in SLUGS.items():
        if slug in cache:
            continue
        try:
            cache[slug] = fetch(slug)
            print(f"  ok    {label:18} {slug}")
        except Exception as exc:                      # noqa: BLE001 - report and continue
            missing.append((label, slug, str(exc)))
            print(f"  MISS  {label:18} {slug}  ({exc})")
    OUT.write_text(json.dumps(cache, indent=0, sort_keys=True))
    print(f"\n{len(cache)} glyphs cached -> {OUT}")
    if missing:
        print("no glyph (these render as text-only chips, which is fine):")
        for label, slug, _ in missing:
            print(f"  {label} ({slug})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
