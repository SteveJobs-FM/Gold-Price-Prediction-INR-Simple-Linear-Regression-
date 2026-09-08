# Ferns & Petals - Sales & Operational Performance Dashboard

An end-to-end Business Intelligence project built using **Advanced Microsoft Excel (Power Query, Power Pivot, DAX)** to analyze revenue trends, seasonal gift demand, customer spending behavior, and supply chain operational efficiency for Ferns & Petals.

---

## 📌 Project Overview
The objective of this project was to engineer a centralized analytical reporting system that transforms fragmented sales data into strategic business insights. By integrating automated ETL pipelines, star-schema data modeling, and interactive visual reporting, this dashboard enables data-driven decision-making across inventory planning, holiday marketing spend, and logistics performance.

* **Core Competencies:** Data Extraction (ETL), Data Cleansing, Star Schema Modeling, DAX Measures, Cohort & Seasonal Analysis, KPI Dashboarding.
* **Tools Used:** Microsoft Excel, Power Query Editor, Power Pivot, DAX (Data Analysis Expressions).

---

## ⚙️ Development Methodology & Pipeline

### 1. Data Extraction & Cleansing (ETL Phase)
* **Ingestion:** Automated multi-source data ingestion (CSV/Excel feeds) via **Power Query Editor** to ensure continuous data refresh capabilities.
* **Data Hygiene:** Handled null/missing records, stripped trailing/leading whitespace, eliminated duplicate transactions, and standardized heterogeneous date/time formats.
* **Feature Engineering:** 
  * Derived temporal features such as `Order Hour` and `Day of Week` from raw order timestamps.
  * Mapped transaction dates to seasonal retail triggers under an engineered `Occasion` category (e.g., Diwali, Valentine’s Day, Raksha Bandhan, Anniversaries).

### 2. Data Modeling & Architecture
* **Relational Schema:** Designed an optimized **Star Schema** within **Power Pivot**, establishing one-to-many (`1:*`) relationships between dimension tables and the central transaction table:
  * **Fact Table:** `Fact_Sales`
  * **Dimension Tables:** `Dim_Customers`, `Dim_Products`, `Dim_Calendar`
* **Analytical Calculations (DAX):** Built robust custom DAX measures for dynamic slice-and-dice capability:
  * **Total Revenue:** Sum of line-item sales values across completed orders.
  * **Total Orders:** Distinct count of valid transactional IDs.
  * **Average Customer Spend (AOV):** Total Revenue divided by Total Orders.
  * **Operational Delivery Cycle:** Dynamic computation of lead-time days (`Delivery Date - Order Date`).

### 3. Interactive Visualization & Dashboarding
* **Visual Layer:** Designed intuitive chart layouts (multi-axis line charts, sorted category column charts, and regional density visuals).
* **Cross-Filtering & Interactivity:** Integrated synchronized **Slicers** (`Order Date`, `Delivery Date`, `Occasion`) to allow business stakeholders to drill down by custom date windows and gifting events with a single click.

---

## 📊 Key Business Insights & Metrics

| Metric | Business Value | Operational Impact |
| :--- | :--- | :--- |
| **Total Revenue** | **₹3,520,984** | Benchmark volume across measured transaction window. |
| **Total Orders** | **1,000** | Stable order generation across multi-city delivery hubs. |
| **Average Order Value (AOV)** | **₹3,520.98** | High basket value indicating premium gifting purchases. |
| **Avg. Delivery Lead Time** | **5.53 Days** | Core SLA benchmark for supply chain optimization. |

* **Seasonal Revenue Drivers:** **Anniversary** and **Raksha Bandhan** campaigns emerged as the primary revenue generators, highlighting key windows for promotional marketing allocation.
* **Product Catalog Mix:** The **"Colors"** merchandise category drove top-tier sales, followed by strong complementary demand in **Soft Toys** and **Sweets**.
* **Tier-2/Tier-3 Regional Penetration:** Cities like **Dhanbad**, **Imphal**, and **Kavali** generated high order volumes, signaling untapped regional growth outside metropolitan centers.

---

## 📁 Repository Structure
```text
├── Data/
│   ├── raw_sales_data.csv          # Source transactional extracts
│   └── product_customer_dim.xlsx   # Dimension lookups
├── Dashboard/
│   └── Ferns_Petals_Sales_BI.xlsx  # Complete model (Power Query, Power Pivot, DAX, Dashboard)
├── Documentation/
│   ├── Data_Model_Schema.png       # Star schema relationship diagram
│   └── Dashboard_Preview.png       # High-resolution dashboard screenshot
└── README.md                       # Project documentation