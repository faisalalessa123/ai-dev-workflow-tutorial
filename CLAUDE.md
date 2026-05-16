# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

A tutorial that teaches students a professional AI-assisted development workflow by having them build and deploy a Streamlit e-commerce sales dashboard. It is primarily a **documentation and curriculum repository** — there is no application code here by default. Students fork and clone this repo, then build the dashboard on a feature branch during the workshop.

## Repository layout

- `v3/` — Current version of the tutorial (Superpowers plugin-based workflow)
  - `pre-work-setup.md` — Tool installation and account setup guide (60–90 min, async)
  - `workshop-build-deploy.md` — Live workshop guide (3 hours)
- `v2/` — Previous version (GitHub spec-kit workflow)
- `v1/` — Original two-session tutorial
- `prd/ecommerce-analytics.md` — The product requirements document students build from
- `data/sales-data.csv` — Sample sales dataset (date, order_id, product, category, region, quantity, unit_price, total_amount)
- `docs/superpowers/` — Created during the workshop by the Superpowers plugin
  - `specs/` — Design documents output by the `brainstorming` skill
  - `plans/` — Implementation plans output by the `writing-plans` skill

## Workflow the tutorial teaches

```
PRD → brainstorming → writing-plans → Jira → Code → Commit → Push → Deploy
```

The Superpowers plugin auto-invokes three skills:
- `brainstorming` — asks clarifying questions, produces a design doc in `docs/superpowers/specs/`
- `writing-plans` — turns the design into a task-by-task implementation plan in `docs/superpowers/plans/`
- `executing-plans` — implements tasks one at a time with TDD for data-transformation tasks

## The Streamlit dashboard students build

Stack: Python 3.11+, Streamlit, Pandas, Plotly. Entry point: `app.py` at repo root (created during workshop). Data source: `data/sales-data.csv`.

To run the dashboard once it exists:
```bash
source venv/bin/activate    # macOS
# or: venv\Scripts\activate  # Windows
streamlit run app.py
# Opens at http://localhost:8501
```

## v3/CLAUDE.md

During the workshop, students create `v3/CLAUDE.md` with project-specific guidance before running Superpowers. That file tells Claude to:
- Work on a feature branch on the main checkout — **do not create git worktrees**
- Use Python 3.11+, idiomatic pandas, and Streamlit components straight from the docs
- Write plain readable code (students need to understand it)

If that file exists and you are helping a student build the dashboard, follow its conventions.

## Jira integration

The workshop connects Claude Code to Jira via the Atlassian MCP server:
```bash
claude mcp add --transport sse atlassian https://mcp.atlassian.com/v1/sse
```
The Jira project key is `ECOM`. Every commit message should include the relevant issue key (e.g., `ECOM-1: add KPI scorecards`).

## Deployment

Students deploy to Streamlit Community Cloud from the `main` branch. The app must have a `requirements.txt` in the repo root listing all dependencies.

<!-- SPECKIT START -->
For additional context about technologies to be used, project structure,
shell commands, and other important information, read the current plan
at `specs/001-analytics-dashboard/plan.md`.
<!-- SPECKIT END -->
