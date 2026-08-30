#!/usr/bin/env python3
"""Generate assets/ledger.svg — the selected-work panel.

GitHub renders markdown in its own grey body type and permits no CSS, so
anything that has to carry the palette must ship as an image. This draws the
evidence table as a designed panel instead of a markdown table.
"""

W = 860
GOLD, FELT, BONE = "#D9B87C", "#2E7D5B", "#E8E3DA"
DIM, KEY, VAL, HAIR = "#5C5665", "#6F6879", "#A9A39A", "#23202A"
BG, PANEL = "#0B0B0D", "#111015"

PAD = 26
ROW = 46
HEAD = 74

# name, stack, domain, the guarantee
ROWS = [
    ("ORCA",         "python · fastapi", "marine safety advisory",  "a refusal you can audit"),
    ("Causa",        "otel · python",    "microservice root-cause", "a verdict you can defend"),
    ("welp",         "rust · sqlite",    "shell failure triage",    "rules, not guesses"),
    ("the house",    "qml · quickshell", "compositor shell",        "a scope it states out loud"),
    ("Replay Trader","kotlin · compose", "market replay",           "same inputs, same session"),
    ("bjak",         "qml",              "six-deck blackjack",      "an edge measured, not claimed"),
]

C1, C2, C3 = PAD + 4, 250, 470     # name | domain | guarantee
HEIGHT = HEAD + ROW * len(ROWS) + 22


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;")


rows = []
for i, (name, stack, domain, guarantee) in enumerate(ROWS):
    y = HEAD + i * ROW
    mid = y + ROW / 2
    rows.append(f'''  <g>
    <text class="name"  x="{C1}" y="{mid - 7}">{esc(name)}</text>
    <text class="stack" x="{C1}" y="{mid + 10}">{esc(stack)}</text>
    <text class="dom"   x="{C2}" y="{mid}">{esc(domain)}</text>
    <text class="gtee"  x="{C3}" y="{mid}">{esc(guarantee)}</text>
  </g>''')
    if i < len(ROWS) - 1:
        rows.append(f'  <line class="hair" x1="{PAD}" y1="{y + ROW}" x2="{W - PAD}" y2="{y + ROW}"/>')

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {HEIGHT}" width="{W}" height="{HEIGHT}" role="img" aria-label="Selected work: ORCA, marine safety advisory, a refusal you can audit. Causa, microservice root-cause, a verdict you can defend. welp, shell failure triage, rules not guesses. the house, compositor shell, a scope it states out loud. Replay Trader, market replay, same inputs same session. bjak, six-deck blackjack, an edge measured not claimed.">
  <title>Selected work {chr(8212)} what each system guarantees</title>
  <style>
    text {{ font-family: "JetBrains Mono", "SFMono-Regular", ui-monospace, Consolas, "Liberation Mono", monospace; }}
    .hdr   {{ font-size: 10.5px; fill: {DIM}; letter-spacing: .18em; }}
    .name  {{ font-size: 15px; fill: {GOLD}; font-weight: 600; }}
    .stack {{ font-size: 10.5px; fill: {KEY}; letter-spacing: .04em; }}
    .dom   {{ font-size: 13px; fill: {VAL}; dominant-baseline: middle; }}
    .gtee  {{ font-size: 13px; fill: {BONE}; dominant-baseline: middle; }}
    .hair  {{ stroke: {HAIR}; stroke-width: 1; }}
  </style>

  <rect x=".5" y=".5" width="{W - 1}" height="{HEIGHT - 1}" rx="10" fill="{BG}" stroke="{HAIR}"/>

  <text class="hdr" x="{C1}" y="34">SELECTED WORK</text>
  <text class="hdr" x="{C2}" y="34">DOMAIN</text>
  <text class="hdr" x="{C3}" y="34">GUARANTEE</text>
  <line class="hair" x1="{PAD}" y1="52" x2="{W - PAD}" y2="52"/>
  <rect x="{C1}" y="44" width="34" height="2" fill="{GOLD}"/>

{chr(10).join(rows)}
</svg>
'''

if __name__ == "__main__":
    import pathlib
    out = pathlib.Path(__file__).with_name("ledger.svg")
    out.write_text(svg)
    print(f"wrote {out}")
