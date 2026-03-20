# CLAUDE.md

This file provides guidance for AI assistants (Claude and others) working in this repository.

## Project Overview

This is a new website project in early initialization. As of the initial commit, no framework, dependencies, or source code have been added yet. This file should be updated as the project grows.

- **Repository**: `kfam227/website`
- **Current State**: Freshly initialized — no framework chosen, no source code, no dependencies
- **Branch convention**: Feature branches follow the pattern `claude/<description>-<id>`

## Repository Structure

```
/
├── README.md       # Minimal project readme
└── CLAUDE.md       # This file
```

Update this section as directories and files are added.

## Development Workflow

### Branching

- Main branch: `main` (or `master`)
- Feature branches: `claude/<feature-description>-<session-id>` for AI-assisted work
- Always develop on the designated feature branch and push before opening a PR

### Git Practices

- Write clear, descriptive commit messages summarizing the *why*, not just the *what*
- Commit related changes together; avoid mixing unrelated changes in one commit
- Always push with: `git push -u origin <branch-name>`
- Never force-push to `main`/`master`

## Setup & Commands

> No commands are defined yet. Update this section once a framework and package manager are chosen.

Typical commands to document here once applicable:
- Install dependencies
- Start development server
- Run tests
- Build for production
- Lint / format

## Tech Stack

> Not yet determined. Update this section once a framework is chosen.

Candidates to document here:
- **Framework**: (e.g., Next.js, Astro, SvelteKit, plain HTML)
- **Language**: (e.g., TypeScript, JavaScript)
- **Styling**: (e.g., Tailwind CSS, CSS Modules, Sass)
- **Testing**: (e.g., Vitest, Jest, Playwright)
- **Package manager**: (e.g., npm, pnpm, yarn)

## Coding Conventions

> Update this section once the stack is decided. General principles in the meantime:

- Prefer simple, focused solutions — avoid over-engineering
- Do not add features, helpers, or abstractions beyond what is explicitly required
- Keep files small and single-purpose
- Validate at system boundaries (user input, external APIs); trust internal code
- Never commit secrets, credentials, or `.env` files

## AI Assistant Guidelines

When working in this repository:

1. **Read before modifying** — always read a file before editing it
2. **Minimal footprint** — only change what is needed; do not refactor surrounding code unless asked
3. **No invented structure** — do not add directories, files, or config that wasn't requested
4. **Update this file** — whenever the tech stack, structure, or conventions change, update `CLAUDE.md` to reflect the current state
5. **Branch discipline** — develop on the designated `claude/` branch; never push to `main` without explicit permission
6. **Confirm destructive actions** — deleting files/branches, force-pushing, or dropping data requires user confirmation first
7. **Commit and push** — after completing implementation tasks, commit with a clear message and push to the feature branch

## Updating This File

This `CLAUDE.md` should be kept current. When you add a framework, dependencies, scripts, or new conventions, update the relevant sections above so future AI sessions start with accurate context.
