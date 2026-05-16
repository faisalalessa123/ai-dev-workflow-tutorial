<!--
SYNC IMPACT REPORT
==================
Version change: (template) → 1.0.0
New constitution — all sections authored from scratch.

Modified principles: N/A (initial ratification)

Added sections:
  - Core Principles (I–V)
  - Technical Standards
  - Development Workflow
  - Governance

Removed sections: N/A

Templates reviewed:
  - .specify/templates/plan-template.md ✅ aligned (Constitution Check gate preserved)
  - .specify/templates/spec-template.md ✅ aligned (no testing mandate conflicts)
  - .specify/templates/tasks-template.md ✅ aligned (tests marked OPTIONAL, consistent with Principle III)

Follow-up TODOs: None — all placeholders resolved.
-->

# E-Commerce Analytics Dashboard Constitution

## Core Principles

### I. Simplicity Over Flexibility

The dashboard MUST expose fixed, pre-defined views optimised for the 80% use case.
Custom filter controls, drill-down interactions, and user-configurable layouts are out of scope.
Every feature decision MUST ask: "does this serve the common daily workflow of a sales or
operations team member?" If the answer requires explanation, the feature is too complex.

### II. Plain, Readable Code

All code MUST be written so a junior developer or student can follow it without additional
explanation. This means:

- No clever abstractions or premature generalisation
- No helper-function layers that obscure intent
- Explicit logic preferred over terse one-liners
- Variable and function names MUST describe what they contain, not how they work

If removing a function and inlining its body makes the code clearer, inline it.

### III. Internal Sales & Operations Focus

The dashboard exists solely to help sales and operations teams monitor KPIs from
`data/sales-data.csv`. Every chart, metric, and label MUST be legible and meaningful to
a non-technical business user. Technical jargon MUST NOT appear in the UI.

### IV. Visual Verification (No Formal Test Suite)

This project carries no automated test suite. Correctness is verified by visual inspection
of the running Streamlit app. As a consequence:

- Data transformation logic MUST be kept simple enough that visual inspection is sufficient
- Each chart MUST be independently verifiable against the raw CSV
- Complexity that cannot be verified visually MUST NOT be introduced

### V. Streamlit Community Cloud Deployment

The app MUST be deployable to Streamlit Community Cloud from the `main` branch at all times.
This means:

- `requirements.txt` at the repo root MUST list every runtime dependency with pinned or
  compatible version specifiers
- The entry point MUST remain `app.py` at the repo root
- No deployment infrastructure beyond Streamlit Community Cloud is permitted for this project
- Every merge to `main` MUST leave the app in a deployable state

## Technical Standards

**Stack**: Python 3.11+, Streamlit, Pandas, Plotly

**Data source**: `data/sales-data.csv` (date, order_id, product, category, region,
quantity, unit_price, total_amount)

**Entry point**: `app.py` at repository root

**Dependency file**: `requirements.txt` at repository root — MUST be kept current

**No database**: All data is loaded from CSV at startup; no external database or API calls

**No authentication**: The app is internal and access-controlled at the hosting level

## Development Workflow

1. Work on a feature branch cut from `main`
2. Build and verify the feature by running `streamlit run app.py` locally
3. Visual inspection MUST confirm all charts render correctly before merge
4. Merge to `main` triggers automatic redeploy on Streamlit Community Cloud
5. Commit messages SHOULD reference the relevant Jira issue key (e.g., `ECOM-1: add KPI scorecards`)

## Governance

This constitution supersedes all other practices and informal agreements for this project.
Amendments require:

1. A clear statement of the principle being changed and the motivation
2. Review by at least one other contributor
3. Version bump per the policy below
4. Update to this file with a revised Sync Impact Report comment

**Versioning policy**:
- MAJOR — backward-incompatible removal or redefinition of a principle
- MINOR — new principle or section added / materially expanded guidance
- PATCH — clarifications, wording fixes, non-semantic refinements

All implementation plans and specifications MUST include a Constitution Check confirming
no principle is violated before work begins.

**Version**: 1.0.0 | **Ratified**: 2026-05-15 | **Last Amended**: 2026-05-15
