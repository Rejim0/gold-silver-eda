Gold & Silver Market Analysis (Exploratory Data Analysis)

Overview
This project is an exploratory data analysis (EDA) of historical gold and silver price data.
The goal was to understand how these two precious metals behave over time, how closely they are related, whether geopolitical risk has any short-term impact on prices, and which asset has performed better in the long run.
The project focuses on understanding patterns, not prediction or trading strategies.
What I Analyzed
I explored the dataset by answering three main questions:
Do gold and silver prices move together over time?
Does geopolitical risk influence daily price changes in gold and silver?
Which asset has delivered better long-term returns (ROI)?
Each question was answered using appropriate statistical measures and visualizations.
Dataset
The dataset contains 10,571 daily observations
Each row represents one trading day
Key columns include:
Gold and silver prices (open, high, low, close)
Daily percentage price changes
Geopolitical Risk Index (GPRD)
Date information spanning multiple decades
Data Cleaning
Before analysis, the dataset was cleaned to ensure reliable results:
Removed the EVENT column due to excessive missing values
Handled missing numerical values using mean imputation
Converted the DATE column to datetime format
Sorted data chronologically for correct time-series analysis
Checked for duplicates (none found)

Key Findings

1. Gold vs Silver Price Relationship
Gold and silver prices show a very strong positive correlation (≈ 0.92).
This indicates that both metals generally move together and respond similarly to market conditions.
A scatter plot clearly shows this strong relationship.

2. Geopolitical Risk vs Daily Price Changes
Daily percentage changes in gold and silver prices show no meaningful linear relationship with the Geopolitical Risk Index (GPRD).
This suggests that:
Short-term price movements are noisy
Geopolitical risk may influence markets over longer horizons rather than daily fluctuations

3. Long-Term Return Comparison (ROI)
After sorting the data chronologically and calculating total returns:
Gold ROI: ~1088%
Silver ROI: ~565%
Gold significantly outperformed silver in terms of long-term price appreciation over the observed period.
A bar chart was used to clearly compare the total returns.
Tools Used
Python
Pandas (data manipulation and analysis)
Matplotlib & Seaborn (visualization)
NumPy (used internally through Pandas)

Project Structure
gold-silver-eda/
│
├── gold_silver.py
├── GoldSilver.csv
├── plots/
│   ├── gold_vs_silver.png
│   ├── gold_change_vs_gprd.png
│   ├── silver_change_vs_gprd.png
│   └── roi_comparison.png
├── README.md
├── .gitignore
└── LICENSE

Takeaways
Gold and silver prices move closely together
Geopolitical risk does not strongly affect daily price changes
Gold has delivered higher long-term returns than silver
Short-term volatility does not necessarily reflect long-term performance

Author
REJIM OLI
Python Exploratory Data Analysis Project
