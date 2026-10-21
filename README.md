## nifty100-regime-estimation

An end-to-end financial intelligence platform for Nifty 100 equity research, financial ratio engine, multi-factor screening, cash flow analytics, KMeans archetype clustering, and automated tearsheet reporting.

Built for the Bluestock Fintech Analytics Internship.

## Install

\\ash
$ pip install -r requirements.txt
\
## Quickstart

\\ash
# Ingest Excel statements into SQLite data warehouse
$ python -m src.etl.loader

# Compute 10-year financial ratios and populate ratio engine
$ python -m src.analytics.ratios

# Run the full test suite (70 tests, 0 failures)
$ pytest tests/ -v

# Launch the interactive Streamlit BI dashboard
$ streamlit run src/dashboard/app.py

# Launch the FastAPI REST server (16 endpoints)
$ uvicorn src.api.main:app --port 8000 --reload

# Batch compile company tearsheets and sector reports
$ python -m src.reports.batch_generation
\
## Features

- **Data Foundation & SQL Warehouse:** Robust ETL pipeline ingesting 10 financial statement datasets for 92 Nifty 100 companies into SQLite (\data/nifty100.db\).
- **Financial Ratio Engine:** 10-year longitudinal computation of ROE, ROCE, D/E, OPM, Interest Coverage, and 5-year CAGRs with negative-base turnaround detection.
- **Investment Screener:** Multi-parameter query engine filtering by ROE, leverage, FCF, and predefined presets ('Quality Compounders', 'Defensive Dividend', 'Value Cyclicals').
- **Cash Flow Intelligence:** Classification by CFO/PAT conversion quality, CapEx intensity, capital allocation patterns, and operational distress flags.
- **Unsupervised ML Clustering:** 5 distinct corporate archetypes derived via StandardScaler and KMeans clustering (k=5).
- **Automated Institutional Reporting:** Batch generation of 92 two-page company tearsheets (eports/tearsheets/\), 11 sector PDF reports (eports/sector/\), and portfolio summaries.
- **FastAPI REST Server:** 16 high-performance endpoints with OpenAPI 3.0 interactive documentation (\/docs\).

## REST API Endpoints

\\	ext
GET /api/v1/health                     # System status and SQLite table row counts
GET /api/v1/companies                  # 92 Nifty 100 companies with filters
GET /api/v1/companies/{ticker}         # Full company profile and latest KPIs
GET /api/v1/companies/{ticker}/pl      # Multi-year Profit & Loss history
GET /api/v1/companies/{ticker}/bs      # Multi-year Balance Sheet history
GET /api/v1/companies/{ticker}/ratios  # 10-year computed financial ratios
GET /api/v1/screener                   # Filter and rank companies by metrics
GET /api/v1/sectors                    # 11 sector summaries and median KPIs
GET /api/v1/sectors/{sector}/companies # All companies within target sector
GET /api/v1/peers/{group_name}         # Peer rankings and percentiles
GET /api/v1/portfolio/stats            # P10 to P90 percentile distribution
\
## Structure

\\	ext
├── config/              # Screener configurations & presets
├── data/
│   ├── raw/             # Raw financial statements (10 Excel files)
│   └── nifty100.db      # SQLite relational data warehouse
├── docs/
│   ├── analyst_guide.pdf       # 12-page analyst user guide (AC-20)
│   ├── acceptance_checklist.pdf# Day 45 signed-off acceptance checklist
│   └── openapi.json            # OpenAPI 3.0 specification
├── output/              # Screener outputs, cash flow KPIs & cluster labels
├── reports/
│   ├── tearsheets/      # 92 company tearsheet PDFs (2 pages each)
│   ├── sector/          # 11 sector PDF reports
│   ├── portfolio/       # Portfolio summary PDF
│   └── pytest_report.html # Full test suite results (70/70 passing)
├── src/
│   ├── analytics/       # Ratios, cash flow KPIs & KMeans clustering
│   ├── api/             # FastAPI application and route handlers
│   ├── dashboard/       # Streamlit multi-screen web interface
│   ├── etl/             # Ingestion, validation, and cleaners
│   ├── nlp/             # Regex parser and auto pros/cons generator
│   └── reports/         # ReportLab tearsheet & sector PDF generators
└── tests/               # 70 unit and integration tests (0 failures)
\
## Deliverables

All 23 project deliverables (D-01 to D-23) completed and verified for Day 45 sign-off. Full audit available in [\docs/acceptance_checklist.pdf\](docs/acceptance_checklist.pdf) and system manual in [\docs/analyst_guide.pdf\](docs/analyst_guide.pdf).

## License

MIT
