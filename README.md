# US Domestic Flights: End-to-End Data Analysis (SQL to Machine Learning)
## Project Overview 
This project encompasses an end-to-end data analysis process to examine the primary factors influencing US domestic flight ticket prices. The main objective is to evaluate the impact of regional airport competition and passenger volume on average ticket prices using statistical hypothesis testing and machine learning algorithms.

## Technologies Used 
**Data Extraction & Processing:** Excel, SQL 
**Data Visualization:** Power BI  
**Programming Language:** Python (pandas, numpy, matplotlib)  
**Statistical Analysis:** scipy.stats 
**Machine Learning:** scikit-learn

## Project Workflow and Key Findings

**1. Data Extraction and Preparation (SQL)**
The core dataset (average_fare_sql.xlsx) was generated using custom SQL queries on the flight database.  State-level average ticket prices, minimum/maximum values, and standard deviation ratios were calculated.  Airports were categorized into three distinct volume tiers (High, Medium, and Low Volume) based on their passenger numbers.  The top five highest and lowest average-fare airports were identified to establish a baseline for exploratory data analysis and reporting.
   
**2. Evaluating the Impact of Competition (Statistical Analysis)**
The hypothesis of whether having multiple airports in a city (local market competition) reduces ticket prices was tested.  Cities with a single airport were grouped against cities with multiple airports, and Welch's Independent T-Test was applied.  Given that the resulting p-value exceeded 0.05, it was proven that local market competition does not create a statistically significant reduction in ticket prices, which was further illustrated via box plots.
   
**3. Predictive Modeling via Machine Learning**
A Simple Linear Regression model was implemented to measure the effectiveness of passenger volume in predicting average ticket prices.  The initial baseline model indicated no meaningful linear relationship between passenger count and ticket prices, with the distribution analyzed using a scatter plot.

**4. Advanced Optimization (Logarithmic Transformation)**
To address extreme data volatility and outliers, a Level-Log transformation (np.log1p) was applied to the passenger volume variable using the numpy library.  Following the logarithmic transformation, the regression model was retrained, yielding a significant improvement in the R-squared score.  The optimized model mathematically demonstrated that a 1% increase in passenger volume results in a marginal, negligible change in ticket prices.

**Note: The "2025" label found within the dataset's column names (e.g., 2025_Passengers_Sample10) is a typo in the original source file; the analyzed data represents the year 2026.**
