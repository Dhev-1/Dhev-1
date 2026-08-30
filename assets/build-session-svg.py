#!/usr/bin/env python3
"""Generate assets/welp-session.svg — the animated terminal header.

SMIL rather than CSS animation: it is what GitHub's camo-proxied SVGs reliably
support, and every element hangs off one shared 12s cycle so the typing, the
caret and the output can never drift apart. Edit the timeline below and re-run;
don't hand-edit the SVG.
"""

CYCLE = 12.0          # seconds, one full loop
FS = 14               # font-size
CH = 8.4              # monospace advance at FS=14 (0.6em)
X = 22                # left gutter
W = 780

GOLD, FELT, BONE = "#D9B87C", "#2E7D5B", "#E8E3DA"
RED, DIM, KEY, VAL, FAINT = "#B4544B", "#5C5665", "#6F6879", "#A9A39A", "#3A3543"

FADE = 0.25           # how long a line takes to arrive
HOLD_END = 10.60      # everything starts leaving here
GONE = 11.10          # and is gone by here


def kt(t):
    """seconds -> keyTime fraction, clamped and rounded."""
    return round(max(0.0, min(1.0, t / CYCLE)), 5)


def typing(elem_id, text, y, start, end):
    """Discrete character reveal: a clip rect parked left of the text, stepped right."""
    n = len(text)
    width = n * CH
    # keyTimes MUST begin at 0 or the whole animation is discarded, so the
    # hidden state is pinned at 0 and held until typing starts.
    values, times = [round(X - width, 2)], [0.0]
    for i in range(n + 1):
        values.append(round(X - width + i * CH, 2))
        times.append(kt(start + (end - start) * (i / n)))
    # hold the finished state for the rest of the cycle
    values.append(X)
    times.append(1.0)
    return (
        f'    <clipPath id="{elem_id}">\n'
        f'      <rect x="{round(X - width, 2)}" y="{y - 14}" width="{width}" height="20">\n'
        f'        <animate attributeName="x" dur="{CYCLE}s" repeatCount="indefinite"\n'
        f'                 calcMode="discrete"\n'
        f'                 values="{";".join(str(v) for v in values)}"\n'
        f'                 keyTimes="{";".join(str(t) for t in times)}"/>\n'
        f'      </rect>\n'
        f'    </clipPath>\n'
    )


def caret(text, y, start, end, vis_from, vis_to):
    """Block cursor that steps along with the typing, then blinks out."""
    n = len(text)
    values, times = [X], [0.0]
    for i in range(n + 1):
        values.append(round(X + i * CH, 2))
        times.append(kt(start + (end - start) * (i / n)))
    values.append(round(X + n * CH, 2))
    times.append(1.0)
    return (
        f'  <rect class="caret" x="{X}" y="{y - 9}" width="8" height="17" opacity="0">\n'
        f'    <animate attributeName="x" dur="{CYCLE}s" repeatCount="indefinite"\n'
        f'             calcMode="discrete"\n'
        f'             values="{";".join(str(v) for v in values)}"\n'
        f'             keyTimes="{";".join(str(t) for t in times)}"/>\n'
        f'    <animate attributeName="opacity" dur="{CYCLE}s" repeatCount="indefinite"\n'
        f'             calcMode="discrete" values="0;1;0;0"\n'
        f'             keyTimes="0;{kt(vis_from)};{kt(vis_to)};1"/>\n'
        f'    <animate attributeName="fill-opacity" dur="0.9s" repeatCount="indefinite"\n'
        f'             calcMode="discrete" values="1;0" keyTimes="0;0.55"/>\n'
        f'  </rect>\n'
    )


def appear(at):
    """Fade a group in at `at`, hold, then clear before the loop restarts."""
    return (
        f'<animate attributeName="opacity" dur="{CYCLE}s" repeatCount="indefinite"\n'
        f'             values="0;0;1;1;0;0"\n'
        f'             keyTimes="0;{kt(at)};{kt(at + FADE)};{kt(HOLD_END)};{kt(GONE)};1"/>'
    )


def persist():
    """Already on screen (the typed lines); just clear before the restart."""
    return (
        f'<animate attributeName="opacity" dur="{CYCLE}s" repeatCount="indefinite"\n'
        f'             values="1;1;0;0"\n'
        f'             keyTimes="0;{kt(HOLD_END)};{kt(GONE)};1"/>'
    )


CMD1 = "$ cargo test --release"
CMD2 = "$ welp"

Y1, Y2, Y3 = 58, 84, 118          # cmd, error, welp
Y4, Y5, Y6, Y7 = 150, 176, 200, 224   # the diagnosis
HEIGHT = 264

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {HEIGHT}" width="{W}" height="{HEIGHT}" role="img" aria-label="Terminal session: cargo test exits 101 with an unhelpful error, then welp reports that the active toolchain is nightly while rust-toolchain.toml pins 1.82.0, and suggests rustup override set 1.82.0">
  <title>welp {chr(8212)} diagnosing a failed cargo test</title>

  <defs>
{typing("typeA", CMD1, Y1, 0.20, 1.50)}{typing("typeB", CMD2, Y3, 2.50, 2.90)}  </defs>

  <style>
    text {{ font-family: "JetBrains Mono", "SFMono-Regular", ui-monospace, Consolas, "Liberation Mono", monospace;
           font-size: {FS}px; dominant-baseline: middle; }}
    .title {{ font-size: 11.5px; fill: {DIM}; letter-spacing: .08em; }}
    .prompt {{ fill: {FELT}; }}
    .cmd    {{ fill: {BONE}; }}
    .err    {{ fill: {RED}; }}
    .fail   {{ fill: {GOLD}; }}
    .meta   {{ fill: {DIM}; }}
    .key    {{ fill: {KEY}; }}
    .val    {{ fill: {VAL}; }}
    .fix    {{ fill: {FELT}; }}
    .arrow  {{ fill: {FAINT}; }}
    .caret  {{ fill: {GOLD}; }}
  </style>

  <rect x=".5" y=".5" width="{W - 1}" height="{HEIGHT - 1}" rx="10" fill="#0B0B0D" stroke="#23202A"/>
  <path d="M .5 10.5 A 10 10 0 0 1 10.5 .5 H {W - 10.5} A 10 10 0 0 1 {W - .5} 10.5 V 34.5 H .5 Z" fill="#111015"/>
  <line x1="0" y1="34.5" x2="{W}" y2="34.5" stroke="#23202A"/>
  <circle cx="22" cy="17.5" r="4.5" fill="{FAINT}"/>
  <circle cx="39" cy="17.5" r="4.5" fill="{FAINT}"/>
  <circle cx="56" cy="17.5" r="4.5" fill="{GOLD}"/>
  <text class="title" x="{W // 2}" y="18" text-anchor="middle">dhev@arch  ~/cloon/wat/welp</text>

  <g clip-path="url(#typeA)">
    <text x="{X}" y="{Y1}" textLength="{len(CMD1) * CH}" lengthAdjust="spacing"><tspan class="prompt">$ </tspan><tspan class="cmd">cargo test {chr(45)}{chr(45)}release</tspan></text>
    {persist()}
  </g>
{caret(CMD1, Y1, 0.20, 1.50, 0.0, 1.75)}
  <g class="err">
    <text x="{X}" y="{Y2}">error: process didn{chr(39)}t exit successfully (exit code: 101)</text>
    {appear(1.90)}
  </g>

  <g clip-path="url(#typeB)">
    <text x="{X}" y="{Y3}" textLength="{len(CMD2) * CH}" lengthAdjust="spacing"><tspan class="prompt">$ </tspan><tspan class="cmd">welp</tspan></text>
    {persist()}
  </g>
{caret(CMD2, Y3, 2.50, 2.90, 2.30, 3.20)}
  <g>
    <text class="fail" x="{X}" y="{Y4}">{chr(10007)} cargo test {chr(45)}{chr(45)}release</text>
    <text class="meta" x="{W - 22}" y="{Y4}" text-anchor="end">exit 101  {chr(183)}  1.8s ago</text>
    {appear(3.30)}
  </g>
  <g>
    <text class="arrow" x="{X}" y="{Y5}">{chr(8627)}</text>
    <text class="key" x="{X + 22}" y="{Y5}">toolchain</text>
    <text class="val" x="{X + 128}" y="{Y5}">nightly-2026-08-02</text>
    {appear(3.55)}
  </g>
  <g>
    <text class="arrow" x="{X}" y="{Y6}">{chr(8627)}</text>
    <text class="key" x="{X + 22}" y="{Y6}">pinned</text>
    <text class="val" x="{X + 128}" y="{Y6}">rust-toolchain.toml wants 1.82.0</text>
    {appear(3.80)}
  </g>
  <g>
    <text class="arrow" x="{X}" y="{Y7}">{chr(8627)}</text>
    <text class="key" x="{X + 22}" y="{Y7}">try</text>
    <text class="fix" x="{X + 128}" y="{Y7}">rustup override set 1.82.0</text>
    {appear(4.05)}
  </g>
</svg>
'''

if __name__ == "__main__":
    import pathlib
    out = pathlib.Path(__file__).with_name("welp-session.svg")
    out.write_text(svg)
    print(f"wrote {out} ({len(svg)} bytes)")
