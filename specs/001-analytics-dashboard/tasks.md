---
description: "Task list for ShopSmart Sales Dashboard"
---

# Tasks: ShopSmart Sales Dashboard

**Input**: Design documents from `specs/001-analytics-dashboard/`

**Prerequisites**: plan.md ✅, spec.md ✅, research.md ✅, data-model.md ✅

**Tests**: Not included — constitution Principle IV specifies visual inspection only.

**Organization**: Tasks follow user story priority order (P1→P4). Each story is
independently implementable and verifiable.

## Format: `[ID] [P?] [Story?] Description`

- **[P]**: Can run in parallel (different concerns, no blocking dependency)
- **[Story]**: Which user story this task belongs to (US1–US4)
- All tasks include exact file paths

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization — all dependencies and the app skeleton ready before
any user story work begins.

- [x] T001 Create `requirements.txt` at repo root with exact-pinned deps: `streamlit==1.45.1`, `pandas==2.2.3`, `plotly==5.24.1`
- [x] T002 Create Python virtual environment (`python -m venv venv`) and install from `requirements.txt`
- [x] T003 Create `app.py` at repo root with: all imports (`streamlit`, `pandas`, `plotly.express`), `st.set_page_config(page_title="ShopSmart Sales Dashboard", layout="wide")`, and a `@st.cache_data` function `load_data()` that reads `data/sales-data.csv` into a DataFrame

**Checkpoint**: `streamlit run app.py` opens at `http://localhost:8501`, page title reads
"ShopSmart Sales Dashboard", no errors in terminal.

---

## Phase 2: User Story 1 — KPI Scorecard (Priority: P1) 🎯 MVP

**Goal**: Display Total Sales and Total Orders as metric cards at the top of the page.

**Independent Test**: Open the dashboard; confirm two metric cards are visible at the top
with Total Sales ~$650K–$700K (currency-formatted) and Total Orders = 482.

- [x] T004 [US1] Add KPI section to `app.py`: compute `total_sales = df['total_amount'].sum()` and `total_orders = len(df)`, display both using `st.metric()` with currency formatting (`f"${total_sales:,.0f}"`) and integer formatting (`f"{total_orders:,}")`

**Checkpoint**: Two metric cards visible and correct. Cross-check values against a manual
sum of the CSV. US1 is fully functional — stop and validate before continuing.

---

## Phase 3: User Story 2 — Monthly Sales Trend (Priority: P2)

**Goal**: Display a monthly line chart showing total sales over 12 months.

**Independent Test**: Line chart shows exactly 12 data points (Jan–Dec); hovering any
point shows the month label and exact sales value.

- [x] T005 [US2] Add trend chart to `app.py`: compute `df['month'] = pd.to_datetime(df['date']).dt.to_period('M').dt.to_timestamp()`, group by month with `groupby('month')['total_amount'].sum().reset_index()`, render with `px.line(monthly, x='month', y='total_amount', title='Sales Trend', labels={'month': 'Month', 'total_amount': 'Total Sales ($)'})`, display with `st.plotly_chart(fig, use_container_width=True)`

**Checkpoint**: 12-point line chart visible below KPI cards; tooltip on hover. US2
independently verified.

---

## Phase 4: User Story 3 — Sales by Category (Priority: P3)

**Goal**: Display a bar chart ranking all 5 product categories by total sales, sorted
highest to lowest.

**Independent Test**: 5 bars visible, sorted descending; hovering shows category name
and exact sales total.

- [x] T006 [US3] Add category chart to `app.py`: aggregate with `df.groupby('category')['total_amount'].sum().reset_index().sort_values('total_amount', ascending=False)`, render with `px.bar(cat_df, x='category', y='total_amount', title='Sales by Category', labels={'category': 'Category', 'total_amount': 'Total Sales ($)'})`, store as `fig_cat` (will be placed in columns in T008)

**Checkpoint**: Category bar chart shows 5 bars sorted highest to lowest with tooltips.
US3 independently verified.

---

## Phase 5: User Story 4 — Sales by Region (Priority: P4)

**Goal**: Display a bar chart ranking all 4 geographic regions by total sales, placed
side-by-side with the category chart.

**Independent Test**: 4 bars visible sorted descending; both bar charts appear in a
two-column layout.

- [x] T007 [US4] Add region chart to `app.py`: aggregate with `df.groupby('region')['total_amount'].sum().reset_index().sort_values('total_amount', ascending=False)`, render with `px.bar(reg_df, x='region', y='total_amount', title='Sales by Region', labels={'region': 'Region', 'total_amount': 'Total Sales ($)'})`, store as `fig_reg`
- [x] T008 [US4] Arrange category and region charts side by side in `app.py` using `col1, col2 = st.columns(2)` with `col1.plotly_chart(fig_cat, use_container_width=True)` and `col2.plotly_chart(fig_reg, use_container_width=True)` (replace any earlier individual `st.plotly_chart` calls for these two charts)

**Checkpoint**: Dashboard shows KPI row → trend chart → two-column bar charts. All four
user stories functional. Full layout matches the PRD mockup.

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Error resilience and final verification.

- [x] T009 Add CSV error handling in `app.py`: wrap the `load_data()` call in a try/except; on failure call `st.error("Unable to load sales data. Please ensure data/sales-data.csv is present.")` and `st.stop()` so no traceback is shown to the user
- [x] T010 Run the quickstart.md visual verification checklist (`specs/001-analytics-dashboard/quickstart.md`) and confirm all items pass; fix any discrepancies before marking done

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies — start immediately
- **US1 (Phase 2)**: Depends on Setup complete — first independently shippable increment
- **US2 (Phase 3)**: Depends on Setup; independent of US1 (different section of app.py)
- **US3 (Phase 4)**: Depends on Setup; independent of US1 and US2
- **US4 (Phase 5)**: Depends on US3 (T008 places both bar charts in columns — fig_cat from T006 must exist)
- **Polish (Phase 6)**: Depends on all user stories complete

### Within Each Phase

- T004 (US1), T005 (US2), T006 (US3) have no cross-story dependencies and can be
  implemented in any order after Setup
- T007 must precede T008 (region chart must exist before the column layout is set up)
- T009 and T010 require all story tasks complete

### User Story Independence Summary

| Story | Can start after | Depends on other stories? |
|-------|----------------|--------------------------|
| US1 — KPI Scorecard | Phase 1 (Setup) | No |
| US2 — Monthly Trend | Phase 1 (Setup) | No |
| US3 — Category Chart | Phase 1 (Setup) | No |
| US4 — Region + Layout | US3 (fig_cat needed for T008) | Yes — US3 only |

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup (T001–T003)
2. Complete Phase 2: US1 KPI Scorecard (T004)
3. **STOP and VALIDATE**: Two metric cards show correct values
4. Demo to stakeholders if needed — this alone delivers the core business value

### Incremental Delivery

1. Setup (T001–T003) → blank page loads ✅
2. US1 (T004) → KPI cards ✅ → Demo/validate
3. US2 (T005) → trend chart ✅ → Demo/validate
4. US3 (T006) → category chart ✅ → Demo/validate
5. US4 (T007–T008) → region chart + layout ✅ → Demo/validate
6. Polish (T009–T010) → production-ready ✅ → Deploy

---

## Notes

- All 10 tasks write to `app.py` — only one developer should work the file at a time
- `[P]` is omitted from all tasks here since the single-file constraint prevents true parallelism
- Each checkpoint is a `streamlit run app.py` visual inspection — no automated tests
- Commit after each phase checkpoint to keep git history clean and reversible
- After T010 passes, the app is ready to deploy per `specs/001-analytics-dashboard/quickstart.md`
