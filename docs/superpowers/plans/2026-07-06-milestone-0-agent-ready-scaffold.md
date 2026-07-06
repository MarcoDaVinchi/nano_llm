# Milestone 0 Agent-Ready Scaffold Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create the minimal durable repository scaffold needed before starting LLM learning experiments.

**Architecture:** This milestone is documentation-and-structure only. It creates the files future agents need to recover context, follow learning guardrails, and start the first Learning Unit without relying on chat history.

**Tech Stack:** Markdown, Makefile, Python 3 standard library for lightweight repository verification.

---

## Chunk 1: Durable project context files

### Task 1: Root learning-project documents

**Files:**
- Create: `README.md`
- Create: `AGENTS.md`
- Create: `MEMORY.md`
- Create: `ROADMAP.md`
- Modify: `CONTEXT.md` only if glossary links need minor alignment

- [ ] **Step 1: Create `README.md`**

Include the project purpose, audience, non-goals, quick start, and current milestone.

- [ ] **Step 2: Create `AGENTS.md`**

Include boot protocol, task modes, anti-overreach, no-hidden-magic, Learning Review, status updates, fresh-context recovery, Go/Python boundary, and completion rules.

- [ ] **Step 3: Create `MEMORY.md`**

Record initial durable session notes and link to the finalized spec.

- [ ] **Step 4: Create `ROADMAP.md`**

Create milestone overview and Learning Unit index. Mark Milestone 0 in progress and Milestone 1 planned.

## Chunk 2: Learning Unit templates and docs indexes

### Task 2: Templates and documentation directories

**Files:**
- Create: `templates/LEARNING.md`
- Create: `templates/STATUS.md`
- Create: `templates/HANDOFF.md`
- Create: `docs/glossary.md`
- Create: `docs/experiments.md`
- Create: `docs/decisions/.gitkeep`
- Create: `experiments/README.md`

- [ ] **Step 1: Create Learning Unit templates**

Keep templates short and operational. They should support fresh-context recovery, not enforce a heavy workflow.

- [ ] **Step 2: Create docs indexes**

Point `docs/glossary.md` to `CONTEXT.md` as the canonical glossary for now. Use `docs/experiments.md` to describe how Learning Units work.

- [ ] **Step 3: Create experiments index**

Explain that no experiment should start until Milestone 0 is complete and Milestone 1 is planned.

## Chunk 3: Minimal repository mechanics

### Task 3: Placeholder directories and verification

**Files:**
- Create: `.gitignore`
- Create: `Makefile`
- Create: `scripts/verify_markdown.py`
- Create: `.gitkeep` placeholders under `cmd/`, `internal/`, `python/`, `data/raw/`, `data/processed/`, `models/checkpoints/`

- [ ] **Step 1: Create ignore rules**

Ignore common OS/editor/build/cache files, Python caches, Go binaries, logs, and large generated model/data artifacts while allowing `.gitkeep` placeholders.

- [ ] **Step 2: Create `Makefile`**

Add `help`, `status`, and `verify` targets. `verify` should run the lightweight markdown checker.

- [ ] **Step 3: Create markdown checker**

Check that Markdown files have balanced fenced code blocks and no tab characters.

- [ ] **Step 4: Run verification**

Run: `make verify`
Expected: all Markdown files pass.

- [ ] **Step 5: Inspect git status**

Run: `git status --short`
Expected: only Milestone 0 scaffold files are modified or untracked.

- [ ] **Step 6: Commit scaffold**

```bash
git add .
git commit -m "chore: add agent-ready learning scaffold"
```
