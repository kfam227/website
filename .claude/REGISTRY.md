# Workshop G — Claude File Registry

> **What this is:** A running log of every file Claude has been given access to, produced, or edited in this project. Updated after each session.
>
> **Protocol:** Whenever Claude generates a new tool, script, or skill, it will prompt you to document it here before closing the session.

---

## Skill-Save Protocol

At the end of any session where Claude produced something new and reusable, Claude will ask:

> "Should I save this as a skill? I'll add a detailed doc to `.claude/skills/` and update the registry."

You can also trigger it manually by saying: **"Save that as a skill."**

Each skill gets:
- A detailed `.md` file in `.claude/skills/`
- An entry in the **Skills & Tools** section below
- A row in **Files Produced**

---

## Files Given Access To

These are files that exist in the project and that Claude has read or been directed to work on.

| File | Path | Type | Date First Accessed |
|------|------|------|---------------------|
| NMThera_BusinessPlan_2026_v3.html | `/HTML/NMThera_BusinessPlan_2026_v3.html` | HTML Document | 2026-03-20 |
| SOKY_Clinical_v1.2.html | `/HTML/SOKY_Clinical_v1.2.html` | HTML Document | 2026-03-20 |
| SOKY_Investor_v1.3.html | `/HTML/SOKY_Investor_v1.3.html` | HTML Document | 2026-03-20 |
| SOKY_LandingVideo_v1.0.html | `/HTML/SOKY_LandingVideo_v1.0.html` | HTML Document | 2026-03-20 |
| SOKY_Manifesto_v2.0.html | `/HTML/SOKY_Manifesto_v2.0.html` | HTML Document | 2026-03-20 |
| settings.local.json | `/.claude/settings.local.json` | Claude Config | 2026-03-20 |

---

## Files Produced by Claude

These are files Claude created from scratch during sessions.

| File | Path | Purpose | Date Created |
|------|------|---------|--------------|
| serve.ps1 | `/serve.ps1` | PowerShell HTTP server — serves the `/HTML` folder locally | 2026-03-20 |
| launch.json | `/.claude/launch.json` | Claude Code preview server configurations (5 HTML docs, ports 8080–8084) | 2026-03-20 |
| static-html-preview-server.md | `/.claude/skills/static-html-preview-server.md` | Skill doc for the preview server setup | 2026-03-20 |
| REGISTRY.md | `/.claude/REGISTRY.md` | This file — master project registry | 2026-03-20 |

---

## Files Edited by Claude

These are existing files Claude has modified during sessions.

| File | Path | What Changed | Date |
|------|------|-------------|------|
| *(none yet)* | | | |

---

## Skills & Tools

Reusable capabilities that have been documented and can be relaunched.

| Skill | Doc | What It Does | Status |
|-------|-----|-------------|--------|
| Static HTML Preview Server | `/.claude/skills/static-html-preview-server.md` | Serves `/HTML` folder via PowerShell + opens live preview panel in Claude Code. No Node/Python needed. | Active |

---

## Project Directory Map

```
NMT_Claude_WorkshopG/               ← Project root
│
├── serve.ps1                        ← [PRODUCED] PowerShell static file server
│
├── HTML/                            ← [ACCESS GRANTED] All original HTML documents
│   ├── NMThera_BusinessPlan_2026_v3.html
│   ├── SOKY_Clinical_v1.2.html
│   ├── SOKY_Investor_v1.3.html
│   ├── SOKY_LandingVideo_v1.0.html
│   └── SOKY_Manifesto_v2.0.html
│
└── .claude/                         ← Claude Code configuration folder
    ├── settings.local.json          ← [ACCESS GRANTED] Claude Code permissions config
    ├── launch.json                  ← [PRODUCED] Preview server launch configurations
    ├── REGISTRY.md                  ← [PRODUCED] This file
    └── skills/
        └── static-html-preview-server.md   ← [PRODUCED] Skill documentation
```

---

*Last updated: 2026-03-20 · Updated by Claude (claude-sonnet-4-6)*
