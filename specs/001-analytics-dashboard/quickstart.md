# Quickstart: ShopSmart Sales Dashboard

**Feature**: `001-analytics-dashboard`
**Date**: 2026-05-15

---

## Prerequisites

- Python 3.11 or later (`python --version`)
- Git (repo already cloned)

---

## Setup

```bash
# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate          # macOS / Linux
# venv\Scripts\activate           # Windows

# Install exact dependencies
pip install -r requirements.txt
```

---

## Run the Dashboard

```bash
streamlit run app.py
```

The dashboard opens automatically at `http://localhost:8501`.

---

## Verify Correctness (Visual Checklist)

Open the dashboard and confirm:

- [x] Page title reads "ShopSmart Sales Dashboard"
- [x] Two KPI cards visible at top: "Total Sales" ($116,500) and "Total Orders" (482)
- [x] Monthly trend line chart shows 12 data points (Jan–Dec)
- [x] Hovering a trend point shows month label and exact value
- [x] Category bar chart shows 5 bars sorted highest → lowest
- [x] Region bar chart shows 4 bars sorted highest → lowest
- [x] Category and region charts are side by side (two columns)
- [x] No Python errors or warnings appear in the terminal

---

## Deploy to Streamlit Community Cloud

1. Push `app.py` and `requirements.txt` to `main` branch on GitHub
2. Log in to [share.streamlit.io](https://share.streamlit.io)
3. Click **New app** → select this repo → set Main file path to `app.py`
4. Click **Deploy** — the app will be live at a public URL within ~2 minutes

---

## Troubleshooting

| Symptom | Fix |
|---------|-----|
| `FileNotFoundError: data/sales-data.csv` | Run `streamlit run app.py` from the repo root, not a subdirectory |
| `ModuleNotFoundError: streamlit` | Activate the virtual environment: `source venv/bin/activate` |
| Blank charts | Check terminal for pandas errors; ensure CSV columns match the data model |
| Wrong KPI values | Cross-check `df['total_amount'].sum()` in a Python REPL against the CSV |
