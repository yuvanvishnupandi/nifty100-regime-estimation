## nifty100-regime-estimation

An end-to-end financial intelligence and market regime estimation engine for the NIFTY 100 universe. Integrates longitudinal financial statement ETL, a 10-year ratio engine, unsupervised KMeans archetype clustering, multi-factor screening, automated institutional PDF tearsheets, and a high-throughput FastAPI service.

Built for the Bluestock Fintech Analytics Internship.

## Install

```bash
$ pip install -r requirements.txt
```

## Quickstart

```python
from src.analytics.clustering import run_kmeans_clustering
from src.analytics.financial_ratios import FinancialRatioEngine

# 1. Compute 10-year longitudinal financial ratios
engine = FinancialRatioEngine(db_path="data/nifty100.db")
ratios_df = engine.compute_all_ratios()

# 2. Derive 5 corporate regime archetypes via KMeans
run_kmeans_clustering()
```

Launch the interactive Streamlit BI dashboard:

```bash
$ streamlit run src/dashboard/app.py
```

Launch the FastAPI REST server (16 endpoints, OpenAPI at `/docs`):

```bash
$ uvicorn src.api.main:app --port 8000 --reload
```

Run the complete test suite (70 tests, 0 failures):

```bash
$ pytest tests/ -v
```

Batch generate 92 institutional tearsheets & 11 sector PDF reports:

```bash
$ python -m src.reports.batch_generation
```

## Features

- **Relational Data Warehouse:** Automated ETL pipeline ingesting 10 financial statement datasets for 92 NIFTY 100 companies into SQLite (`data/nifty100.db`).
- **10-Year Ratio Engine:** Longitudinal computations of ROE, ROCE, D/E, OPM, Interest Coverage, and 5-year CAGRs with negative-base turnaround heuristics.
- **Regime Archetype Clustering:** Unsupervised KMeans (k=5) with standard scaling segmenting corporate operating regimes (High-Quality Compounders, Capital Intensive, Leveraged Growth, Cyclical Recovery, Stable Yield).
- **Multi-Factor Screener:** Quantitative filtering engine supporting pre-built investment presets (`Quality Compounders`, `Defensive Dividend`, `Value Cyclicals`).
- **Institutional Reporting:** Batch compilation of 92 institutional 2-page company tearsheets (`reports/tearsheets/`), 11 sector reports (`reports/sector/`), and portfolio summaries.
- **Production REST API:** 16 OpenAPI 3.0 endpoints for company fundamentals, historical statements, peer percentiles, and screener queries.

## REST API Endpoints

```text
GET  /api/v1/health                     # Health check & table row diagnostics
GET  /api/v1/companies                  # 92 NIFTY 100 constituent profiles
GET  /api/v1/companies/{ticker}         # Company fundamentals & latest KPIs
GET  /api/v1/companies/{ticker}/pl      # Multi-year Profit & Loss history
GET  /api/v1/companies/{ticker}/bs      # Multi-year Balance Sheet records
GET  /api/v1/companies/{ticker}/ratios  # 10-year computed ratio time series
GET  /api/v1/screener                   # Multi-factor metric screening & ranking
GET  /api/v1/sectors                    # 11 sector summaries and median KPIs
GET  /api/v1/sectors/{sector}/companies # Constituent breakdown by sector
GET  /api/v1/peers/{group_name}         # Industry peer ranking and percentiles
GET  /api/v1/portfolio/stats            # Decile distributions (P10 - P90)
```

## Structure

```text
.
|-- config/             # Screener presets & factor thresholds
|-- data/
|   |-- raw/            # 10 raw financial statement datasets
|   `-- nifty100.db     # SQLite financial data warehouse
|-- docs/
|   |-- analyst_guide.pdf       # 12-page comprehensive analyst user guide
|   |-- acceptance_checklist.pdf# Completed Day 45 formal sign-off checklist
|   `-- openapi.json            # OpenAPI 3.0 specification
|-- output/             # Screen results, cash flow KPIs & cluster labels
|-- reports/
|   |-- tearsheets/     # 92 institutional 2-page company tearsheets
|   |-- sector/         # 11 sector macroeconomic PDF reports
|   `-- portfolio/      # Portfolio summary report
|-- src/
|   |-- analytics/      # Ratios, cash flow analytics & KMeans clustering
|   |-- api/            # FastAPI application, routers & middlewares
|   |-- dashboard/      # Streamlit multi-screen visual analytics
|   |-- etl/            # Statement parsers, loaders & cleaners
|   |-- nlp/            # Automated qualitative pros/cons generator
|   `-- reports/        # ReportLab institutional PDF engines
`-- tests/              # 70 unit and integration tests (0 failures)
```

## Deliverables

All 23 project deliverables (D-01 to D-23) completed and verified for Day 45 sign-off:
- **Analyst Guide:** [docs/analyst_guide.pdf](docs/analyst_guide.pdf) (12 pages)
- **Acceptance Checklist:** [docs/acceptance_checklist.pdf](docs/acceptance_checklist.pdf)
- **Test Suite Report:** [reports/pytest_report.html](reports/pytest_report.html) (70/70 passing)

## Citations

```bibtex
@software{yuvan2026nifty100,
  author    = {Yuvan Vishnu Pandi},
  title     = {NIFTY 100 Financial Intelligence & Regime Estimation Platform},
  year      = {2026},
  publisher = {GitHub},
  journal   = {GitHub repository},
  howpublished = {\url{https://github.com/yuvanvishnupandi/nifty100-regime-estimation}}
}
```

## License

MIT
