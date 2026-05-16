# Research: ShopSmart Sales Dashboard

**Feature**: `001-analytics-dashboard`
**Date**: 2026-05-15
**Status**: Complete — all unknowns resolved

---

## Decision 1: Code Structure

**Decision**: Single `app.py` file at repository root

**Rationale**: The constitution (Principle II) requires plain, readable code that a student
can follow without explanation. A single file lets a reader trace the entire application
top-to-bottom. Streamlit's own "getting started" examples use this pattern.

**Alternatives considered**:
- `app.py` + `data.py` — rejected; the added indirection costs more than it saves for
  ~60 lines of data logic
- `app.py` + `data.py` + `charts.py` — rejected; over-engineering for a four-chart dashboard

---

## Decision 2: CSV Caching

**Decision**: Wrap the CSV load in `@st.cache_data`

**Rationale**: Streamlit re-runs the entire script on every user interaction. Without
caching, `pd.read_csv()` fires on every rerender — harmless for 1,000 rows but bad
practice. `@st.cache_data` is the standard Streamlit pattern and adds only one decorator
line, keeping code readable.

**Alternatives considered**:
- No caching — rejected; re-reading the file on every interaction is wasteful and
  teaches bad habits even if unnoticeable at this data size

---

## Decision 3: Plotly API Style

**Decision**: Use Plotly Express (`import plotly.express as px`)

**Rationale**: Plotly Express produces interactive charts in one line. `px.line()` and
`px.bar()` match the chart types required by the spec. Plotly Graph Objects (`go.Figure`)
offer more control but require 5–10× more code for the same output — violating Principle II.

**Key API calls**:
- `px.line(df, x="month", y="total_amount")` — monthly trend chart
- `px.bar(df, x="category", y="total_amount")` — category breakdown
- `px.bar(df, x="region", y="total_amount")` — region breakdown
- `st.metric(label, value)` — KPI scorecard cards

**Alternatives considered**:
- Plotly Graph Objects — rejected; more verbose with no user-visible benefit here
- Altair / Matplotlib — rejected; not in the constitution-mandated stack

---

## Decision 4: Monthly Aggregation Approach

**Decision**: Parse `date` column as datetime, floor to month-start, then `groupby`

**Rationale**: Pandas `pd.to_datetime()` + `dt.to_period('M')` or `resample('MS')`
are both idiomatic. Using `resample` requires setting the index; using `dt.to_period`
with `groupby` is more explicit and readable for students.

**Concrete approach**:
```python
df['month'] = pd.to_datetime(df['date']).dt.to_period('M').dt.to_timestamp()
monthly = df.groupby('month')['total_amount'].sum().reset_index()
```

**Alternatives considered**:
- `resample('MS')` — equally correct but requires date as index, adding an implicit step
- String slicing on the date column — fragile; rejects

---

## Decision 5: Dependency Versions (Exact Pins)

**Decision**: Pin all three runtime dependencies to currently-installed versions

| Package | Pinned Version |
|---------|---------------|
| streamlit | 1.45.1 |
| pandas | 2.2.3 |
| plotly | 5.24.1 |

**Rationale**: Exact pins (`==`) guarantee that every deploy — local, CI, Streamlit
Community Cloud — uses identical library versions. This prevents silent breakage from
upstream releases.

**Alternatives considered**:
- Compatible release (`~=`) — rejected; allows patch updates that could break the deploy
- Minimum version (`>=`) — rejected; allows any future version including breaking changes
