<div align="center">

<img src="./assets/welp-session.svg" alt="A terminal session: cargo test exits 101 with an unhelpful error, then welp explains that the active toolchain is nightly while rust-toolchain.toml pins 1.82.0" width="100%" />

<br/><br/>

### Dhev Arjun A I

**Systems that can explain themselves.**

<img src="https://img.shields.io/badge/Chennai,%20India-0B0B0D?style=flat-square&logo=googlemaps&logoColor=D9B87C&labelColor=0B0B0D" alt="Chennai, India"/>
&nbsp;
<img src="https://img.shields.io/badge/Arch%20%2B%20Hyprland-0B0B0D?style=flat-square&logo=archlinux&logoColor=D9B87C&labelColor=0B0B0D" alt="Arch Linux with Hyprland"/>
&nbsp;
<img src="https://img.shields.io/badge/Deterministic%20by%20default-0B0B0D?style=flat-square&logo=gnubash&logoColor=2E7D5B&labelColor=0B0B0D" alt="Deterministic by default"/>

</div>

---

## The through-line

Most of what I build comes back to one idea: **a system should be able to account for its own
output.** Same inputs, same result, every time — and when it refuses, or ranks something, or
prices something, it can say exactly why.

That isn't an aesthetic preference. It's what makes a marine safety advisory auditable, a
root-cause verdict defensible, a replayed trading session reproducible, and a house edge a
measured number rather than a claimed one. Four unrelated-looking projects, one argument.

The corollary is that I write things down. Every repo here has a real README, a stated scope,
and — usually — a paragraph about what it deliberately does *not* do.

---

## Selected work

> **Note** — these live in private repos while I clean them up. Descriptions are accurate;
> links land as they go public.

### ORCA — Oceanic Reasoning & Constraint Architecture
`Python` `FastAPI` · *Team ICARUS · SIH26176, ISRO Software Challenge*

A marine advisory and safety system for Indian fishermen, fusing ISRO, INCOIS, DGLL and NOAA
feeds into go/no-go guidance. The reasoning layer can be probabilistic; **the safety policy
cannot** — every hard constraint is deterministic Python, so a refusal is reproducible and
traceable to the data that caused it. 103 pytest cases plus 12 end-to-end, and 100% data
provenance through the schema.

### Causa — deterministic root-cause analysis
`OpenTelemetry` `Python` · *distributed tracing*

When a microservice fleet breaks, half of it lights up at once. The hard question isn't what's
on fire — it's which failure is the **cause** and which are downstream victims. Causa
reconstructs an incident as a set of dependency graphs, ranks the most probable root-cause
service with a confidence score and a plain-language *why*, then routes a human-gated
remediation through a canary deploy.

### welp — triage for the command that just failed
`Rust` `SQLite`

A shell hook that diagnoses your last failed command from context the shell **already had** —
exit code, toolchain state, config on disk, recent history. Rules, not guesses; no model call,
no network, and a binary small enough that the hook never makes your prompt feel slow. The
header above is what it actually prints.

### the house — a compositor shell for Hyprland
`QML` `Quickshell` · *and `edge`, its minimal sibling*

A screen border, a bar, a window dock, and the notification daemon, replacing dunst. Pure QML —
no C++ plugin, no build step: clone it and point `qs` at it. One shell, four palettes, switched
live. There is deliberately no dashboard, no OSD and no notification centre; a notification is a
popup and nothing else, and once it leaves the screen it's gone.

Its login screen, **The Door**, is an SDDM greeter where authenticating is a hand of blackjack —
your password types itself onto the felt as a stack of clay chips instead of a row of asterisks.

### Replay Trader — market replay, without the drift
`Kotlin` `Jetpack Compose`

Scrub to a past week, press play, and trade the tape one candle at a time — brackets, shorting,
margin, a full session summary, on a hand-rolled candlestick chart with pinch-zoom and a
drag-to-scale price axis. The engine reads no wall clock and draws no randomness, so identical
inputs replay identically. All money is integers; there is no floating-point drift anywhere in
the accounting.

### Also

| | | |
|---|---|---|
| **Tickin** | helpdesk platform | Angular 22 · ASP.NET Core 9 · Postgres — status lifecycle enforced by an immutable state machine, EF Core optimistic concurrency, SLA background jobs |
| **Kingsman** | service-business platform | NestJS monorepo — one versioned REST API, three clients, 26 recorded architecture decisions and no manual fallback path |
| **Duet Draw** | real-time collaboration | React · Socket.IO — a shared canvas for exactly two people, with the wire protocol typed once and imported by both ends |
| **bjak** *et al.* | Quickshell casino widgets | six-deck blackjack at a **0.46% house edge, measured rather than claimed**; single-zero roulette at 2.70%; 9/6 video poker |
| **AttendIQ** | smart attendance | rotating-QR sessions with geofence verification, built as a runnable local prototype of a Flutter/Firebase PRD |
| **Portfolio** | Astro static site | hand-written CSS, GSAP + Lenis motion layer, no UI framework and no Tailwind |

<!-- ──────────────────────────────────────────────────────────────────────────
     Repo pin cards — uncomment each line as the repo goes public.
     Themed to match: champagne gold on black lacquer.

<div align="center">
<a href="https://github.com/Dhev-1/ORCA"><img src="https://github-readme-stats.vercel.app/api/pin/?username=Dhev-1&repo=ORCA&hide_border=true&bg_color=0B0B0D&title_color=D9B87C&text_color=A9A39A&icon_color=2E7D5B" alt="ORCA"/></a>
<a href="https://github.com/Dhev-1/causa"><img src="https://github-readme-stats.vercel.app/api/pin/?username=Dhev-1&repo=causa&hide_border=true&bg_color=0B0B0D&title_color=D9B87C&text_color=A9A39A&icon_color=2E7D5B" alt="Causa"/></a>
<a href="https://github.com/Dhev-1/welp"><img src="https://github-readme-stats.vercel.app/api/pin/?username=Dhev-1&repo=welp&hide_border=true&bg_color=0B0B0D&title_color=D9B87C&text_color=A9A39A&icon_color=2E7D5B" alt="welp"/></a>
<a href="https://github.com/Dhev-1/dotfiles"><img src="https://github-readme-stats.vercel.app/api/pin/?username=Dhev-1&repo=dotfiles&hide_border=true&bg_color=0B0B0D&title_color=D9B87C&text_color=A9A39A&icon_color=2E7D5B" alt="dotfiles"/></a>
</div>
────────────────────────────────────────────────────────────────────────── -->

---

## Stack

<div align="center">

<img src="https://skillicons.dev/icons?i=rust,py,ts,cpp,kotlin,cs,dart,bash&perline=8" alt="Rust, Python, TypeScript, C++, Kotlin, C#, Dart, Bash" />
<br/>
<img src="https://skillicons.dev/icons?i=fastapi,nestjs,dotnet,nodejs,react,angular,astro,qt&perline=8" alt="FastAPI, NestJS, .NET, Node.js, React, Angular, Astro, Qt/QML" />
<br/>
<img src="https://skillicons.dev/icons?i=postgres,sqlite,docker,githubactions,git,linux,arch,flutter&perline=8" alt="PostgreSQL, SQLite, Docker, GitHub Actions, Git, Linux, Arch, Flutter" />

</div>

**Systems & languages** &nbsp; ![Rust](https://img.shields.io/badge/Rust-0B0B0D?style=flat-square&logo=rust&logoColor=D9B87C) ![C++](https://img.shields.io/badge/C%2B%2B-0B0B0D?style=flat-square&logo=cplusplus&logoColor=D9B87C) ![Python](https://img.shields.io/badge/Python-0B0B0D?style=flat-square&logo=python&logoColor=D9B87C) ![Kotlin](https://img.shields.io/badge/Kotlin-0B0B0D?style=flat-square&logo=kotlin&logoColor=D9B87C) ![C#](https://img.shields.io/badge/C%23-0B0B0D?style=flat-square&logo=csharp&logoColor=D9B87C) ![QML](https://img.shields.io/badge/QML-0B0B0D?style=flat-square&logo=qt&logoColor=D9B87C) ![Bash](https://img.shields.io/badge/Bash-0B0B0D?style=flat-square&logo=gnubash&logoColor=D9B87C) ![Yacc / Lex](https://img.shields.io/badge/FLEX%20%2F%20BISON-0B0B0D?style=flat-square&logoColor=D9B87C)

**Backend & data** &nbsp; ![FastAPI](https://img.shields.io/badge/FastAPI-0B0B0D?style=flat-square&logo=fastapi&logoColor=2E7D5B) ![NestJS](https://img.shields.io/badge/NestJS-0B0B0D?style=flat-square&logo=nestjs&logoColor=2E7D5B) ![ASP.NET Core](https://img.shields.io/badge/ASP.NET%20Core-0B0B0D?style=flat-square&logo=dotnet&logoColor=2E7D5B) ![Express](https://img.shields.io/badge/Express-0B0B0D?style=flat-square&logo=express&logoColor=2E7D5B) ![Socket.IO](https://img.shields.io/badge/Socket.IO-0B0B0D?style=flat-square&logo=socketdotio&logoColor=2E7D5B) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-0B0B0D?style=flat-square&logo=postgresql&logoColor=2E7D5B) ![SQLite](https://img.shields.io/badge/SQLite-0B0B0D?style=flat-square&logo=sqlite&logoColor=2E7D5B) ![Prisma](https://img.shields.io/badge/Prisma-0B0B0D?style=flat-square&logo=prisma&logoColor=2E7D5B)

**Frontend** &nbsp; ![React](https://img.shields.io/badge/React-0B0B0D?style=flat-square&logo=react&logoColor=A9A39A) ![Angular](https://img.shields.io/badge/Angular-0B0B0D?style=flat-square&logo=angular&logoColor=A9A39A) ![Astro](https://img.shields.io/badge/Astro-0B0B0D?style=flat-square&logo=astro&logoColor=A9A39A) ![TypeScript](https://img.shields.io/badge/TypeScript-0B0B0D?style=flat-square&logo=typescript&logoColor=A9A39A) ![Jetpack Compose](https://img.shields.io/badge/Jetpack%20Compose-0B0B0D?style=flat-square&logo=jetpackcompose&logoColor=A9A39A) ![Flutter](https://img.shields.io/badge/Flutter-0B0B0D?style=flat-square&logo=flutter&logoColor=A9A39A) ![GSAP](https://img.shields.io/badge/GSAP-0B0B0D?style=flat-square&logo=greensock&logoColor=A9A39A)

**Infrastructure & rigor** &nbsp; ![Docker](https://img.shields.io/badge/Docker-0B0B0D?style=flat-square&logo=docker&logoColor=D9B87C) ![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-0B0B0D?style=flat-square&logo=githubactions&logoColor=D9B87C) ![OpenTelemetry](https://img.shields.io/badge/OpenTelemetry-0B0B0D?style=flat-square&logo=opentelemetry&logoColor=D9B87C) ![pytest](https://img.shields.io/badge/pytest-0B0B0D?style=flat-square&logo=pytest&logoColor=D9B87C) ![Vitest](https://img.shields.io/badge/Vitest-0B0B0D?style=flat-square&logo=vitest&logoColor=D9B87C) ![insta](https://img.shields.io/badge/insta%20snapshots-0B0B0D?style=flat-square&logoColor=D9B87C)

**Desktop & Linux** &nbsp; ![Arch](https://img.shields.io/badge/Arch%20Linux-0B0B0D?style=flat-square&logo=archlinux&logoColor=2E7D5B) ![Hyprland](https://img.shields.io/badge/Hyprland-0B0B0D?style=flat-square&logo=hyprland&logoColor=2E7D5B) ![Wayland](https://img.shields.io/badge/Wayland-0B0B0D?style=flat-square&logo=wayland&logoColor=2E7D5B) ![Quickshell](https://img.shields.io/badge/Quickshell-0B0B0D?style=flat-square&logo=qt&logoColor=2E7D5B) ![kitty](https://img.shields.io/badge/kitty-0B0B0D?style=flat-square&logo=kitty&logoColor=2E7D5B) ![Zsh](https://img.shields.io/badge/Zsh-0B0B0D?style=flat-square&logo=zsh&logoColor=2E7D5B) ![Neovim](https://img.shields.io/badge/Neovim-0B0B0D?style=flat-square&logo=neovim&logoColor=2E7D5B)

---

## Currently

- Hardening **ORCA**'s deterministic safety policy and its data-provenance schema
- Teaching **welp** more rules — the goal is that it is right often enough to trust silently
- Folding the casino widgets into **the house** as first-class layer-shell surfaces
- Reading more compiler and distributed-systems material than is strictly good for me

**Open to** — open source in Linux/Wayland tooling, developer CLIs, and anything where
"explain your answer" is a hard requirement rather than a nice-to-have.

<!-- ──────────────────────────────────────────────────────────────────────────
     GitHub analytics — held back until the real repos are public, so the
     numbers match the work above. Uncomment then.

<div align="center">
<img src="https://github-readme-stats.vercel.app/api?username=Dhev-1&show_icons=true&hide_border=true&bg_color=0B0B0D&title_color=D9B87C&icon_color=2E7D5B&text_color=A9A39A&ring_color=D9B87C" height="170" alt="GitHub stats"/>
&nbsp;
<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=Dhev-1&layout=compact&hide_border=true&bg_color=0B0B0D&title_color=D9B87C&text_color=A9A39A" height="170" alt="Top languages"/>
<br/><br/>
<img src="https://streak-stats.demolab.com/?user=Dhev-1&hide_border=true&background=0B0B0D&ring=D9B87C&fire=2E7D5B&currStreakLabel=D9B87C&sideLabels=A9A39A&dates=5C5665&stroke=23202A&sideNums=E8E3DA&currStreakNum=D9B87C" alt="Contribution streak"/>
</div>
────────────────────────────────────────────────────────────────────────── -->

---

<div align="center">

<a href="mailto:dhevarjun006@gmail.com"><img src="https://img.shields.io/badge/Email-0B0B0D?style=flat-square&logo=maildotru&logoColor=D9B87C&labelColor=0B0B0D" alt="Email"/></a>
&nbsp;
<a href="https://www.linkedin.com/in/dhev-arjun"><img src="https://img.shields.io/badge/LinkedIn-0B0B0D?style=flat-square&logo=linkedin&logoColor=D9B87C&labelColor=0B0B0D" alt="LinkedIn"/></a>
&nbsp;
<a href="https://orcid.org/0009-0008-5686-4680"><img src="https://img.shields.io/badge/ORCID-0B0B0D?style=flat-square&logo=orcid&logoColor=D9B87C&labelColor=0B0B0D" alt="ORCID 0009-0008-5686-4680"/></a>

<br/><br/>

<sub><i>the edge is measured, not claimed</i> &nbsp;♠</sub>

</div>
