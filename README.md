# Gold Price Prediction (INR) - Simple Linear Regression

## Project Overview
The primary objective was to create an end-to-end Machine Learning pipeline to analyze and predict domestic 22K gold prices in India based on USD/INR exchange rate dynamics. By leveraging automated market data ingestion (`yfinance`), statistical data engineering, Ordinary Least Squares (OLS) regression modeling, and Gradio for deployment, the project provides a dynamic interface to evaluate currency sensitivity and forecast gold rates.

---

## Development Methodology
The project followed a structured data pipeline to ensure data integrity and analytical depth:

### Data Extraction (ETL Phase)
* **Process:** Automated live historical market feeds for USD/INR Forex (`INR=X`) and COMEX Gold Futures (`GC=F`) directly via the `yfinance` API.
* **Goal:** Establish a reliable and reproducible connection to financial sources for real-time market tracking.

### Data Cleaning
* **Refinement:** Flattened nested MultiIndex DataFrame columns down to clean 1D arrays using `.squeeze()` to eliminate downstream dimensional issues.
* **Quality Control:** Handled missing rows (~3.11%) caused by non-synchronized international trading holidays between US and Indian markets by applying Missing Completely At Random (MCAR < 5%) removal rules without introducing bias.

### Data Transformation
* **Feature Engineering:** Converted international 24-Karat COMEX pricing quoted in USD per Troy Ounce into domestic retail metrics (INR per gram, 22-Karat purity) using the formula:
  $$\text{Gold Price (INR/g)} = \left(\frac{\text{Gold\_USD\_oz}}{31.1034768}\right) \times \text{USD\_INR} \times \left(\frac{22}{24}\right)$$
* **Feature Scaling:** Applied `StandardScaler` to normalize the input feature distribution while isolating scaling strictly to training splits to prevent data leakage.

### Data Modeling
* **Architecture:** Formulated and trained a Simple Linear Regression model using `scikit-learn`.
* **Mathematical Calibration:** Analyzed the derived regression line parameters ($y = mx + c$) to quantify economic sensitivity:
  * **Learned Slope ($m$):** ₹525.40 increase in domestic 22K gold price for every 1-unit increase in the scaled USD/INR rate.
  * **Intercept ($c$):** ₹8,332.29 baseline pricing anchor.
* **Hyperparameter Validation:** Tested parameter space optimization using `RandomizedSearchCV`, confirming the analytical closed-form nature of OLS linear regression.

### Data Analysis & Evaluation
* **Evaluation Metrics:** Computed Root Mean Squared Error (RMSE) and $R^2$ Score across training and chronological test splits.
* **Macro Regime-Shift Insights:** Evaluated chronological time-series behavior (`shuffle=False`), revealing the limitations of single-variable linear modeling during periods where international bullion decouples from currency rate movements due to external global market shocks.

### Deployment (MLOps)
* **Pipeline Serialization:** Preserved the trained regression model (`GoldPrice_pred.pkl`) and the preprocessor (`scaled_data.pkl`) using `pickle`.
* **Interactive UI:** Built a web-based prediction interface using `Gradio`, enabling users to input custom exchange rates and receive instantaneous per-gram retail gold estimates.

---

## Key Insights from the Model
* **Currency Sensitivity:** Domestic gold prices exhibit strong sensitivity to the US Dollar, demonstrating a positive slope parameter where rupee depreciation directly amplifies domestic procurement costs.
* **In-Sample Fit:** In-sample training yields an $R^2$ score of 0.316 and an RMSE of ₹772.82, confirming baseline linear correlation during standard market regimes.
* **Out-of-Sample Regime Decoupling:** Forward out-of-sample testing exposed how global geopolitical demand shocks affect commodity levels independently of currency conversion rates.
* **Practical Utility:** The deployed Gradio application provides a lightweight tool for domestic retail gold valuation without the computational overhead of complex deep learning architectures.

---

## Conclusion
Through the systematic application of API data extraction, statistical preprocessing, unit conversion, and MLOps deployment, this project transforms raw market feeds into a functional machine learning deliverable. It provides technical competence in regression modeling while critically analyzing the boundary conditions and limitations of linear estimators in macroeconomic time-series forecasting.
