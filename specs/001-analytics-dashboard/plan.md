# Implementation Plan: ShopSmart Sales Dashboard

**Branch**: `001-analytics-dashboard` | **Date**: 2026-05-15 | **Spec**: [spec.md](spec.md)

**Input**: Feature specification from `specs/001-analytics-dashboard/spec.md`

## Summary

Build a single-page Streamlit dashboard titled "ShopSmart Sales Dashboard" that loads
`data/sales-data.csv` once at startup (cached), displays two KPI metric cards (Total Sales,
Total Orders), a monthly sales trend line chart, and two side-by-side bar charts (sales by
category and by region). All code lives in a single `app.py` at the repository root. No
filters, no authentication, no test suite — correctness verified by visual inspection.

## Technical Context

**Language/Version**: Python 3.11+

**Primary Dependencies**:
- `streamlit==1.45.1` — UI framework and layout
- `pandas==2.2.3` — CSV loading and aggregations
- `plotly==5.24.1` — Interactive charts via Plotly Express

**Storage**: CSV file only — `data/sales-data.csv` (no database)

**Testing**: None — visual inspection per constitution Principle IV

**Target Platform**: Streamlit Community Cloud (web browser)

**Project Type**: Single-page web application

**Performance Goals**: Full page load under 5 seconds; chart render under 2 seconds

**Constraints**: Single `app.py` file; no external APIs; no user input controls;
`requirements.txt` must use exact version pins (`==`)

**Scale/Scope**: ~1,000 CSV rows; 4 charts; 2 KPI metrics; one developer

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Gate | Status |
|-----------|------|--------|
| I. Simplicity Over Flexibility | No custom filters or user controls; fixed views only | ✅ PASS |
| II. Plain, Readable Code | Single `app.py`; Plotly Express (simple API); no abstraction layers | ✅ PASS |
| III. Sales & Operations Focus | KPI cards + trend + category + region — all serve the target audience | ✅ PASS |
| IV. Visual Verification | No test suite; all verification done by running the app | ✅ PASS |
| V. Community Cloud Deployment | `app.py` at root; `requirements.txt` with exact pins; deploy from `main` | ✅ PASS |

All gates pass. No complexity justification required.

## Project Structure

### Documentation (this feature)

```text
specs/001-analytics-dashboard/
├── plan.md              # This file
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output
├── quickstart.md        # Phase 1 output
└── tasks.md             # Phase 2 output (/speckit-tasks command)
```

### Source Code (repository root)

```text
app.py                  # Single-file Streamlit application (entry point)
requirements.txt        # Exact-pinned runtime dependencies
data/
└── sales-data.csv      # Source data (already present in repo)
```

**Structure Decision**: Single-file layout. All data loading, aggregation, and chart
rendering live in `app.py`. This satisfies Principle II (plain, readable code) and
matches Streamlit Community Cloud's expectation of an `app.py` entry point.
