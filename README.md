# US Domestic Flight Price Analysis (Q1 2026)

End-to-end data analytics project on U.S. domestic airport-level average airfares — from raw data cleaning to SQL analysis, a Power BI dashboard, and Python statistical modeling.

## Project Overview

This project analyzes average domestic ticket fares across 613 U.S. airports (54 states) for Q1 2026, using U.S. Bureau of Transportation Statistics data. The goal was to identify what actually drives fare differences between airports — passenger volume, market competition, or state/region — and to build a recruiter-facing dashboard summarizing the findings.

**Pipeline:** Raw data → SQL Server cleaning & analysis → Power BI dashboard → Python statistical testing (regression + hypothesis testing)

## Data Source

- **`average_fare_sql.xlsx`** — raw source file (616 rows: 613 airports + 3 footer/source-note rows), one row per airport.
- Fields: passenger rank, airport code/name, city, state, average fare, inflation-adjusted average fare (base quarter Q1 2026), and a 10% passenger sample count.
- Source: U.S. Bureau of Transportation Statistics.

## Pipeline

### 1. Data Cleaning (SQL Server)
- Removed the 3 non-data footer rows (source/notes text, not records).
- Renamed columns to SQL-safe snake_case (e.g. `Average Fare ($)` → `Average_Fare`).
- Verified data types and checked for nulls.
- Output: **`Flight_Dashboard_Data.xlsx`** — 613 rows, 8 columns, zero nulls. Used as the single source of truth for the dashboard.

### 2. SQL Analysis — `Flight_Analyze.sql`
Queries run against the cleaned table in SQL Server:
- State-level summary: average/min/max/stdev fare, airport count, and total passenger sample per state.
- In-state fare ranking with `RANK() OVER (PARTITION BY State_Name ...)`.
- Inflation impact: nominal vs. inflation-adjusted fare and % change, by state.
- Volume-tier segmentation with `NTILE(3)`: airports split into High / Mid / Low passenger-volume tiers, compared by average fare.
- Cheapest 5 and most expensive 5 airports.
- Intra-city competition: cities with more than one airport, and their average fare.
- Passenger sample share: each airport's % of the total sampled passenger volume.

### 3. Power BI Dashboard
Built from `Flight_Dashboard_Data.xlsx`. Includes:
- Choropleth map of average ticket price by state
- City-based average ticket price bar chart
- Top-15 busiest hubs treemap ("Market Dominance")
- Cheapest 5 / Most Expensive 5 airport tables
- Average ticket price by volume tier (bar chart)
- KPI cards: 613 airports, 54 states

### 4. Python Statistical Analysis
- **`fare_prediction.py`** — linear regression of `Average_Fare` on passenger volume, run both on raw volume and log-transformed volume.
- **`ticket_price_distribution_of_cities_by_number_of_airports.py`** — Welch's t-test comparing average fares in single-airport cities vs. multi-airport (competitive) cities.

## Key Findings

- **Volume alone barely explains fare.** Linear regression of fare on raw passenger volume: **R² = 0.0018**, coefficient ≈ **$0.000046** per additional passenger — practically no relationship.
- **Log-transforming volume helps only slightly.** R² rises to **0.122**; a 1% increase in passenger volume is associated with only a **~$0.14** increase in average fare.
- **Fare doesn't scale simply with hub size.** The volume-tier breakdown shows **Mid-volume airports have the highest average fare ($479)**, ahead of High-volume ($436), while **Low-volume airports have the lowest ($304)** — the opposite of a simple "bigger hub → cheaper due to competition" story. Fare looks more tied to route mix and market structure than to raw traffic.
- **Intra-city airport competition shows no statistically significant effect.** Multi-airport cities average **$431.76** (n=50) vs. **$403.95** (n=563) for single-airport cities — but a Welch's t-test gives **t = -1.09, p = 0.28**, so the difference isn't statistically demonstrable at this sample size.
- Analysis spans **613 airports across 54 states**.

## Tools & Tech Stack

- **SQL Server** — data cleaning, aggregation, window functions
- **Power BI** — dashboard and visualization
- **Python** — pandas, numpy, scikit-learn, scipy, matplotlib, seaborn

## How to Reproduce

1. Load `average_fare_sql.xlsx` into SQL Server and run `Flight_Analyze.sql` top to bottom.
2. Export the cleaned table to `Flight_Dashboard_Data.xlsx`.
3. Import it into Power BI and rebuild the visuals shown in the dashboard PDF.
4. Run the two Python scripts (requires `pandas`, `numpy`, `scikit-learn`, `scipy`, `matplotlib`, `seaborn`) for the regression and hypothesis-testing analysis.

## Limitations

- Single-quarter snapshot (Q1 2026) — no time dimension, so trend/seasonality analysis isn't possible with this dataset alone.
- Airport-level aggregates only; no route-level, distance, or carrier data, which likely explain more fare variance than volume does.
- The competition t-test groups are imbalanced (n=563 vs. n=50), which limits statistical power to detect a real but smaller effect.

## Author

Kaan
