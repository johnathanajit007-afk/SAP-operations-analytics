# SAP S/4HANA Operations Analytics & SLA Dashboard

## Executive Summary
This enterprise data pipeline and automated reporting framework simulates and ingests logistics data from SAP S/4HANA (`VBAK`, `VBAP`, `LIKP`, `LIPS` schemas). It automates On-Time In-Full (OTIF) SLA breach tracking, identifies regional fulfillment latency, and outputs executive auditing dashboards using Python, SQL, and Excel VBA.

The project supports both local synthetic ERP data generation and live cloud integration with the SAP Business Accelerator Hub via OData REST APIs.

## Key Features & Architecture
1. **Cloud & Telemetry Ingestion (`fetch_sap_sandbox.py` & `generate_sap_data.py`):** 
   - Queries live SAP S/4HANA Cloud REST APIs (`API_SALES_ORDER_SRV`) via OData protocol.
   - Generates multi-table relational ERP schemas (`VBAK` Sales Headers, `LIKP` Delivery Notes) in SQLite.
2. **SQL Analytics Engine (`process_sap_data.py`):** 
   - Aggregates fulfillment metrics, calculates OTIF %, and flags regional depot SLA breaches.
3. **VBA Report Automation (`Automate_SLA_Report.bas`):** 
   - Formats raw audit output, applies conditional executive styling, and highlights compliance breaches (<85% OTIF).

## Tech Stack
- **ERP Data Schemas:** SAP S/4HANA (`VBAK`, `VBAP`, `LIKP`, `LIPS`)
- **Protocols & APIs:** REST API, OData, SAP Business Accelerator Hub
- **Languages & Tools:** Python 3.x, SQL (SQLite), Excel VBA, Git/GitHub
- **Data Analytics:** Data Pipelines, SLA Tracking, Operational Bottleneck Identification

## Project Setup & Execution

```bash
# 1. Ingest Data (Choose Option A or B)
# Option A: Ingest Live SAP Sandbox Data via OData API
python fetch_sap_sandbox.py

# Option B: Generate Local Relational SAP Database
python generate_sap_data.py

# 2. Run SQL KPI Aggregation & OTIF Analysis
python process_sap_data.py

# 3. Format Audit Dashboard in Excel
# Open sap_sla_kpi_summary.csv in Excel and run macro Automate_SLA_Report.bas