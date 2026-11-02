# Simple Sales Data Analysis - Retail Store
import pandas as pd
import matplotlib.pyplot as plt

# ---------- Step 1: Data banana ----------
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"] * 3,
    "Category": ["Electronics"] * 6 + ["Clothing"] * 6 + ["Grocery"] * 6,
    "Units_Sold": [40, 35, 50, 45, 55, 60,
                   120, 110, 130, 140, 125, 150,
                   400, 420, 410, 430, 450, 460],
    "Revenue": [200000, 175000, 250000, 225000, 275000, 300000,
                96000, 88000, 104000, 112000, 100000, 120000,
                80000, 84000, 82000, 86000, 90000, 92000],
    "Profit": [30000, 24500, 40000, 31500, 44000, 51000,
               19200, 15840, 22880, 25760, 20000, 28800,
               8000, 9240, 7380, 9460, 9900, 11040],
}
df = pd.DataFrame(data)
df.to_csv("sales_data.csv", index=False)

print("===== DATA (first 6 rows) =====")
print(df.head(6))

# ---------- Step 2: Analysis ----------
# Q1. Category wise total revenue and profit
category_total = df.groupby("Category")[["Revenue", "Profit"]].sum()
print("\n===== Q1: Category wise Total =====")
print(category_total)

# Q2. Month wise total revenue
month_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
month_total = df.groupby("Month")["Revenue"].sum().reindex(month_order)
print("\n===== Q2: Month wise Revenue =====")
print(month_total)
print("Best Month:", month_total.idxmax())

# Q3. Profit margin % of each category
category_total["Profit_Margin_%"] = (category_total["Profit"] / category_total["Revenue"] * 100).round(2)
print("\n===== Q3: Profit Margin % =====")
print(category_total["Profit_Margin_%"])
print("Highest margin category:", category_total["Profit_Margin_%"].idxmax())

# ---------- Step 3: Charts ----------
# Chart 1: Category wise revenue
category_total["Revenue"].plot(kind="bar", color=["#e67e22", "#2980b9", "#27ae60"])
plt.title("Category wise Total Revenue")
plt.ylabel("Revenue (Rs)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("chart1_category_revenue.png")
plt.close()

# Chart 2: Monthly revenue trend
month_total.plot(kind="line", marker="o", color="purple")
plt.title("Monthly Revenue Trend")
plt.ylabel("Revenue (Rs)")
plt.grid(True)
plt.tight_layout()
plt.savefig("chart2_monthly_trend.png")
plt.close()

# Chart 3: Profit margin
category_total["Profit_Margin_%"].plot(kind="bar", color="teal")
plt.title("Profit Margin % by Category")
plt.ylabel("Profit Margin (%)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("chart3_profit_margin.png")
plt.close()

print("\nCharts saved!")
