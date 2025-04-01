import pandas as pd
import os

# Create output directory
os.makedirs('dashboard_output', exist_ok=True)

# Load dataset
df = pd.read_excel(r'C:\Users\sravy\Downloads\Sales Project\data\Sample_Superstore.xls')
print(df.head())

# Convert dates
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Add Profit Margin
df['Profit Margin'] = df['Profit'] / df['Sales']

# Monthly Sales Trend
df['Month'] = df['Order Date'].dt.to_period('M')
monthly_sales = df.groupby('Month')['Sales'].sum()

# Plot
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))
monthly_sales.plot(kind='line', marker='o')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('dashboard_output/monthly_sales_trend.png')
plt.show()
