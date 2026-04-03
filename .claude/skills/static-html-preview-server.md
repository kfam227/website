# Skill: Static HTML Preview Server

**Created:** 2026-03-20
**Created by:** Claude (claude-sonnet-4-6)
**Status:** Active — tested and working

---

## What This Does

Spins up a local HTTP server that serves all `.html` files from the `/HTML` folder, and opens a live preview panel directly inside Claude Code. No Node.js or Python required — uses PowerShell's built-in `System.Net.HttpListener`.

The preview panel lets you:
- See the rendered HTML in real time as Claude makes edits
- Refresh the panel after each change to verify the result
- Navigate between all 5 HTML documents from an index page

---

## Files Created

Both files live in the project root: `NMT_Claude_WorkshopG/`

```
NMT_Claude_WorkshopG/
├── serve.ps1                   ← The PowerShell HTTP server script
├── .claude/
│   └── launch.json             ← Server configs for the Claude Code preview panel
└── HTML/                       ← The folder being served
    ├── NMThera_BusinessPlan_2026_v3.html
    ├── SOKY_Clinical_v1.2.html
    ├── SOKY_Investor_v1.3.html
    ├── SOKY_LandingVideo_v1.0.html
    └── SOKY_Manifesto_v2.0.html
```

---

## File Details

### `serve.ps1` — PowerShell Static File Server

**Full path:** `C:\Users\Administrator\Desktop\NMT_Claude_WorkshopG\serve.ps1`

Accepts a `-Port` parameter (default: 8080). On startup it:
1. Binds to `http://localhost:<port>/`
2. Serves any file inside the `/HTML` folder by path
3. Returns an index page listing all `.html` files when you hit the root `/`
4. Handles MIME types for `.html`, `.css`, `.js`, `.png`, `.jpg`, `.svg`
5. Returns 404 for anything not found

**To run manually from PowerShell:**
```powershell
cd C:\Users\Administrator\Desktop\NMT_Claude_WorkshopG
powershell -ExecutionPolicy Bypass -File serve.ps1 -Port 8080
```

**Then open in browser:**
```
http://localhost:8080/
http://localhost:8080/NMThera_BusinessPlan_2026_v3.html
```

---

### `.claude/launch.json` — Claude Code Preview Configurations

**Full path:** `C:\Users\Administrator\Desktop\NMT_Claude_WorkshopG\.claude\launch.json`

Defines 5 named server entries, one per HTML document, each on its own port:

| Name | File | Port |
|------|------|------|
| Business Plan | NMThera_BusinessPlan_2026_v3.html | 8080 |
| Clinical Deck | SOKY_Clinical_v1.2.html | 8081 |
| Investor Deck | SOKY_Investor_v1.3.html | 8082 |
| Landing Video | SOKY_LandingVideo_v1.0.html | 8083 |
| Manifesto | SOKY_Manifesto_v2.0.html | 8084 |

Uses `bash.exe` (from Git for Windows at `C:\Program Files\Git\usr\bin\bash.exe`) as the runtime executable, which in turn calls `powershell` to run `serve.ps1`. This workaround was necessary because the Claude Preview tool couldn't resolve `powershell` by short name — the full bash path was required.

---

## How to Relaunch the Preview

Tell Claude: **"Start the Business Plan preview"** (or any of the named servers).
Claude will call `preview_start` with that name, read `launch.json`, and open the panel.

Or ask Claude to start multiple at once — each gets its own port and its own panel.

---

## Why This Approach

- No Node.js, Python, or any package manager is installed on this machine
- Git for Windows (bash.exe) is the only available runtime bridge
- PowerShell's `HttpListener` is available natively on all Windows 10+ machines
- The workaround (`bash → powershell`) is stable and tested

---

## Dependencies

| Dependency | Status | Notes |
|---|---|---|
| Git for Windows | Required | Provides `bash.exe` at `C:\Program Files\Git\usr\bin\bash.exe` |
| Windows PowerShell | Required | Built into Windows 10 — no install needed |
| Node.js / Python | Not required | Would simplify `launch.json` if installed in future |

---

## If You Move the Project

If you move `NMT_Claude_WorkshopG/` to a different path, update the hardcoded paths in `.claude/launch.json` — specifically the `-File` argument in each `runtimeArgs` entry. The `serve.ps1` script itself uses `$PSScriptRoot` and is path-agnostic.
