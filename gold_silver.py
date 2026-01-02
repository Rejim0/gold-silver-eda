import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

print("Exploratory Data Analysis and Insight Generation from Real-World Data")

df = pd.read_csv("GoldSilver.csv")
# Display the first few rows
print(df.head().to_string())
# Number of rows and columns
print("Number of rows and columns: ",df.shape)
# Column names
print("Columns Name: ",list(df.columns))
print("\nData Types:")
print(df.info())

print("\nMissing values: \n",df.isna().sum())
print("\nDuplicate Rows Number: ",df.duplicated().sum())

print("\n One row represent the gold and silver price movement in each particular day i.e. how high and low they go"
      " and their % change.Also hows geopolitical risk and threats. ")


# Handle missing values (if any)
df = df.drop(columns=['EVENT'])
cols_to_fill = [
    "GPRD","GPRD_ACT","GPRD_THREAT","SILVER_PRICE","SILVER_OPEN","SILVER_HIGH","SILVER_LOW","SILVER_CHANGE_%"
]
df[cols_to_fill] = df[cols_to_fill].fillna(df[cols_to_fill].mean())

df["DATE"] = pd.to_datetime(df["DATE"])
print("I have made few changes on dataset by calculating mean and adding them on missing part of the columns. I have"
      "changed the date object type to date time.")



#Do gold and silver prices move together over time?
correlation_Gold_Silver = df["GOLD_PRICE"].corr(df["SILVER_PRICE"])
print("\nCorrelation  of Price of GOLD and SILVER:",correlation_Gold_Silver)
plt.figure(figsize=(8,6))
plt.scatter(df["GOLD_PRICE"],df["SILVER_PRICE"],s =12,alpha=0.4,color="steelblue")
plt.xlabel("Gold Price")
plt.ylabel("Silver Price")
plt.title("Relationship Between Gold and Silver Prices")
plt.grid(True,linestyle="--",alpha = 0.5)
plt.savefig("gold_vs_silver.png", dpi=300, bbox_inches="tight")
plt.show()
print("The scatter plot and correlation analysis reveal a very "
      "strong positive relationship between gold and silver prices, "
      "with a correlation coefficient of 0.92. The upward trend \nin the scatter "
      "plot indicates that increases in gold prices are typically accompanied by increases in silver prices, "
      "suggesting that both metals respond similarly to market conditions over time.")

#What is the relationship between geopolitical risk (GPRD) and daily percentage changes in gold and silver prices?
correlation_GPRD_GOLD = df["GOLD_CHANGE_%"].corr(df["GPRD"])
print("\nCorrelation  of change of % GOLD and GPRD:",correlation_GPRD_GOLD)
plt.figure(figsize=(8,6))
plt.scatter(df["GOLD_CHANGE_%"],df["GPRD"],s =12,alpha=0.4,color="steelblue")
plt.xlabel("Gold CHANGE %")
plt.ylabel("GPRD")
plt.title("Relationship Between Gold % Change and GPRD")
plt.grid(True,linestyle="--",alpha = 0.5)
plt.savefig("gold_change_vs_gprd.png", dpi=300, bbox_inches="tight")
plt.show()

correlation_GPRD_SILVER = df["SILVER_CHANGE_%"].corr(df["GPRD"])
print("Correlation  of Change of silver % and GPRD:",correlation_GPRD_SILVER)
plt.figure(figsize=(8,6))
plt.scatter(df["SILVER_CHANGE_%"],df["GPRD"],s =12,alpha=0.4,color="steelblue")
plt.xlabel("SILVER CHANGE %")
plt.ylabel("GPRD")
plt.title("Relationship Between SILVER CHANGE % and GPRD")
plt.grid(True,linestyle="--",alpha = 0.5)
plt.savefig("silver_change_vs_gprd.png", dpi=300, bbox_inches="tight")
plt.show()
print("Correlation analysis shows that geopolitical risk (GPRD) has no meaningful"
      " linear relationship with daily percentage changes in either gold or silver prices."
      " The correlation coefficients for \nboth metals are close to zero, and the scatter plots"
      " show no discernible trend. This indicates that short-term price movements in gold and silver"
      " are largely independent of day-to-day fluctuations in geopolitical risk.")

df = df.sort_values("DATE")
price_gold = (df["GOLD_PRICE"].iloc[-1] - df["GOLD_PRICE"].iloc[0] )/ df["GOLD_PRICE"].iloc[0]
ROI_RETURN_GOLD = round(price_gold * 100,3)
print(f"Till now GOLD gave return of: {ROI_RETURN_GOLD}%")

price_silver = (df["SILVER_PRICE"].iloc[-1]-df["SILVER_PRICE"].iloc[0])/df["SILVER_PRICE"].iloc[0]
ROI_RETURN_SILVER = round(price_silver * 100,3)
print(f"Till now SILVER gave return of: {ROI_RETURN_SILVER}%")

roi_df = pd.DataFrame({
  "ASSET":["GOLD","SILVER"],
    "ROI (%)":[ROI_RETURN_GOLD,ROI_RETURN_SILVER]
})

plt.figure(figsize=(6,7))
sb.barplot(data = roi_df, x = "ASSET", y = "ROI (%)")
plt.title("Total Return Comparison: Gold vs Silver")
plt.ylabel("ROI (%)")
plt.xlabel("Asset")
plt.savefig("roi_comparison.png", dpi=300, bbox_inches="tight")
plt.show()