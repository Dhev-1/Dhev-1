#!/usr/bin/env python3
"""Generate the hero, stack and 'currently' panels.

GitHub renders markdown in its own grey body type and allows no CSS, so every
element that has to carry the palette ships as a hand-authored SVG. Animation
is SMIL, which survives GitHub's image proxy; CSS animation does not reliably.

Run:  python3 assets/build-panels.py
"""

import pathlib

W = 860
GOLD, FELT, BONE = "#D9B87C", "#2E7D5B", "#E8E3DA"
DIM, KEY, VAL, HAIR = "#5C5665", "#6F6879", "#A9A39A", "#23202A"
BG, PANEL = "#0B0B0D", "#141218"

MONO = ('"JetBrains Mono", "SFMono-Regular", ui-monospace, Consolas, '
        '"Liberation Mono", monospace')
CH12 = 7.2      # advance at font-size 12
CH13 = 7.8

HERE = pathlib.Path(__file__).parent


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def chip(x, y, label, h=24, fs=12, fill=VAL, stroke=HAIR, ch=CH12):
    """A pill with the text centred; returns (markup, width)."""
    w = round(len(label) * ch + 22, 1)
    m = (f'<g><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{h/2}" '
         f'fill="none" stroke="{stroke}"/>'
         f'<text x="{round(x + w/2, 1)}" y="{y + h/2 + 0.5}" font-size="{fs}" fill="{fill}" '
         f'text-anchor="middle" dominant-baseline="middle">{esc(label)}</text></g>')
    return m, w


# ── hero ────────────────────────────────────────────────────────────────────
NAME = "DHEV ARJUN A I"
PHRASES = [
    "systems that can explain themselves",
    "same inputs, same result, every time",
    "deterministic by default",
]
HERO_H = 202

chips, cx = [], 40
for c in ("Chennai, India", "Arch + Hyprland", "Rust · Python · QML"):
    m, w = chip(cx, 156, c, stroke="#3A3444")
    chips.append(m)
    cx += w + 10

# each phrase owns a slot of the shared cycle so they can never overlap
slot = 1.0 / len(PHRASES)
phrase_markup = []
for i, p in enumerate(PHRASES):
    a, b = i * slot, (i + 1) * slot
    fade = 0.022
    phrase_markup.append(
        f'    <text class="phrase" x="42" y="127" opacity="0">{esc(p)}\n'
        f'      <animate attributeName="opacity" dur="13.5s" repeatCount="indefinite"\n'
        f'               values="0;0;1;1;0;0"\n'
        f'               keyTimes="0;{round(a,4)};{round(a+fade,4)};'
        f'{round(b-fade,4)};{round(b,4)};1"/>\n'
        f'    </text>')

hero = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {HERO_H}" width="{W}" height="{HERO_H}" role="img" aria-label="Dhev Arjun A I — systems that can explain themselves. Chennai, India. Arch plus Hyprland. Rust, Python, QML.">
  <title>Dhev Arjun A I {chr(8212)} systems that can explain themselves</title>
  <defs>
    <linearGradient id="sweep" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%"   stop-color="{GOLD}" stop-opacity="0"/>
      <stop offset="50%"  stop-color="{GOLD}" stop-opacity="0.5"/>
      <stop offset="100%" stop-color="{GOLD}" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="felt" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%"   stop-color="{FELT}" stop-opacity="0.16"/>
      <stop offset="100%" stop-color="{FELT}" stop-opacity="0"/>
    </linearGradient>
    <clipPath id="panel">
      <rect x="0" y="0" width="{W}" height="{HERO_H}" rx="12"/>
    </clipPath>
  </defs>
  <style>
    text {{ font-family: {MONO}; }}
    .name   {{ font-size: 47px; font-weight: 700; fill: {GOLD}; letter-spacing: .045em; }}
    .phrase {{ font-size: 14.5px; fill: {VAL}; letter-spacing: .02em; }}
    .mark   {{ font-size: 176px; fill: {GOLD}; opacity: .045; }}
  </style>

  <rect x=".5" y=".5" width="{W-1}" height="{HERO_H-1}" rx="12" fill="{BG}" stroke="{HAIR}"/>
  <g clip-path="url(#panel)">
    <rect x="0" y="0" width="{W}" height="{HERO_H}" fill="url(#felt)"/>
    <text class="mark" x="{W-52}" y="172" text-anchor="end">{chr(9824)}</text>

    <!-- a slow gold sweep, the only thing that moves until you look closer -->
    <rect x="-260" y="0" width="260" height="{HERO_H}" fill="url(#sweep)" opacity=".5">
      <animate attributeName="x" values="-260;{W}" dur="7s" repeatCount="indefinite"/>
    </rect>

    <text class="name" x="40" y="76">{esc(NAME)}</text>

    <rect x="42" y="97" height="2" width="0" fill="{GOLD}">
      <animate attributeName="width" values="0;236" dur="1.1s" begin="0.2s" fill="freeze"/>
    </rect>

{chr(10).join(phrase_markup)}

{chr(10).join("    " + c for c in chips)}
  </g>
</svg>
'''

# ── stack ───────────────────────────────────────────────────────────────────
GROUPS = [
    ("LANGUAGES", ["Rust", "Python", "TypeScript", "C++", "Kotlin", "C#", "QML", "Bash"]),
    ("BACKEND",   ["FastAPI", "NestJS", "ASP.NET Core", "Socket.IO",
                   "PostgreSQL", "SQLite", "Prisma"]),
    ("FRONTEND",  ["React", "Angular", "Astro", "Jetpack Compose", "Flutter", "GSAP"]),
    ("RIGOR",     ["Docker", "GitHub Actions", "OpenTelemetry", "pytest", "Vitest",
                   "insta"]),
    ("DESKTOP",   ["Arch", "Hyprland", "Wayland", "Quickshell", "kitty", "Zsh", "Neovim"]),
]

LABEL_X, ITEM_X, MAXW = 30, 168, W - 40
rows, y = [], 46
for name, items in GROUPS:
    rows.append(f'  <text class="glabel" x="{LABEL_X}" y="{y + 12}">{esc(name)}</text>')
    x, line_top = ITEM_X, y
    for it in items:
        m, w = chip(x, y, it, h=25, fs=12)
        if x + w > MAXW:                       # wrap
            x = ITEM_X
            y += 33
            m, w = chip(x, y, it, h=25, fs=12)
        rows.append("  " + m)
        x += w + 8
    y += 33
    if (name, items) != GROUPS[-1]:
        rows.append(f'  <line x1="{LABEL_X}" y1="{y - 4}" x2="{W - 30}" y2="{y - 4}" stroke="{HAIR}"/>')
        y += 14

STACK_H = y + 12
stack = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {STACK_H}" width="{W}" height="{STACK_H}" role="img" aria-label="Stack. {'. '.join(g + ': ' + ', '.join(i) for g, i in GROUPS)}.">
  <title>Stack</title>
  <style>
    text {{ font-family: {MONO}; }}
    .glabel {{ font-size: 10.5px; fill: {GOLD}; letter-spacing: .18em; }}
  </style>
  <rect x=".5" y=".5" width="{W-1}" height="{STACK_H-1}" rx="10" fill="{BG}" stroke="{HAIR}"/>
{chr(10).join(rows)}
</svg>
'''

# ── currently ───────────────────────────────────────────────────────────────
NOW = [
    ("ORCA",         "hardening the deterministic safety policy", 0.72),
    ("welp",         "more rules, until it earns silent trust",   0.55),
    ("the house",    "folding the widgets into layer-shell",      0.40),
    ("reading",      "compilers, distributed systems",            0.85),
]

BAR_X, BAR_W = 560, 250
nrows, y = [], 74
for i, (what, detail, frac) in enumerate(NOW):
    nrows.append(f'''  <g>
    <text class="what" x="30" y="{y}">{esc(what)}</text>
    <text class="det"  x="150" y="{y}">{esc(detail)}</text>
    <rect x="{BAR_X}" y="{y - 5}" width="{BAR_W}" height="4" rx="2" fill="{HAIR}"/>
    <rect x="{BAR_X}" y="{y - 5}" width="0" height="4" rx="2" fill="{FELT}">
      <animate attributeName="width" values="0;{round(BAR_W * frac)}" dur="1.1s"
               begin="{round(0.35 + i * 0.18, 2)}s" fill="freeze"/>
    </rect>
  </g>''')
    y += 40

NOW_H = y + 6
now = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {NOW_H}" width="{W}" height="{NOW_H}" role="img" aria-label="Currently: {'; '.join(f'{w} — {d}' for w, d, _ in NOW)}.">
  <title>Currently</title>
  <style>
    text {{ font-family: {MONO}; dominant-baseline: middle; }}
    .hdr  {{ font-size: 10.5px; fill: {DIM}; letter-spacing: .18em; }}
    .what {{ font-size: 13.5px; fill: {GOLD}; }}
    .det  {{ font-size: 13px; fill: {VAL}; }}
  </style>
  <rect x=".5" y=".5" width="{W-1}" height="{NOW_H-1}" rx="10" fill="{BG}" stroke="{HAIR}"/>
  <text class="hdr" x="30" y="34">CURRENTLY</text>
  <rect x="30" y="44" width="34" height="2" fill="{GOLD}"/>
  <line x1="30" y1="52" x2="{W-30}" y2="52" stroke="{HAIR}"/>
{chr(10).join(nrows)}
</svg>
'''

if __name__ == "__main__":
    for fname, body in (("hero.svg", hero), ("stack.svg", stack), ("now.svg", now)):
        (HERE / fname).write_text(body)
        print(f"wrote {HERE / fname}")
