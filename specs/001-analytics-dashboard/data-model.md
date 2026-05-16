# Data Model: ShopSmart Sales Dashboard

**Feature**: `001-analytics-dashboard`
**Date**: 2026-05-15

---

## Source Entity: Transaction (raw CSV row)

Loaded from `data/sales-data.csv` via `pd.read_csv()`.

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| date | string → datetime | Transaction date | `2024-01-15` |
| order_id | string | Unique order identifier | `ORD-001234` |
| product | string | Product name | `Wireless Headphones` |
| category | string | Product category (5 values) | `Electronics` |
| region | string | Geographic region (4 values) | `North` |
| quantity | int | Units sold | `2` |
| unit_price | float | Price per unit | `49.99` |
| total_amount | float | Total transaction value | `99.98` |

**Validation rules**:
- `date` must parse successfully as `YYYY-MM-DD`; fail loudly if not
- `total_amount` must be non-negative
- `category` must be one of: Electronics, Accessories, Audio, Wearables, Smart Home
- `region` must be one of: North, South, East, West

---

## Derived Entity: KPI Metrics

Computed once from the full Transaction dataset.

| Metric | Derivation | Format |
|--------|-----------|--------|
| Total Sales | `df['total_amount'].sum()` | `$X,XXX,XXX` (currency) |
| Total Orders | `len(df)` or `df['order_id'].count()` | Integer with comma separator |

Rendered via `st.metric()`.

---

## Derived Entity: Monthly Aggregate

One row per calendar month; used for the trend line chart.

| Field | Type | Derivation |
|-------|------|-----------|
| month | datetime (month-start) | `pd.to_datetime(df['date']).dt.to_period('M').dt.to_timestamp()` |
| total_amount | float | `groupby('month')['total_amount'].sum()` |

Sorted ascending by `month` (chronological order).

---

## Derived Entity: Category Aggregate

One row per product category; used for the category bar chart.

| Field | Type | Derivation |
|-------|------|-----------|
| category | string | `groupby('category')['total_amount'].sum()` |
| total_amount | float | Sum of `total_amount` per category |

Sorted descending by `total_amount` (highest category first).

---

## Derived Entity: Region Aggregate

One row per geographic region; used for the region bar chart.

| Field | Type | Derivation |
|-------|------|-----------|
| region | string | `groupby('region')['total_amount'].sum()` |
| total_amount | float | Sum of `total_amount` per region |

Sorted descending by `total_amount` (highest region first).

---

## Data Flow

```
data/sales-data.csv
       │
       ▼  pd.read_csv()  [@st.cache_data]
   DataFrame (raw Transactions)
       │
       ├──► KPI Metrics        → st.metric() cards
       ├──► Monthly Aggregate  → px.line() trend chart
       ├──► Category Aggregate → px.bar() category chart
       └──► Region Aggregate   → px.bar() region chart
```

No data is written back to disk. All derived entities are computed in memory on each
fresh app session (cached across rerenders within the same session).
