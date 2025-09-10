import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_excel("Sales_Data.xlsx", engine="openpyxl", na_values=[])

# Clean Discount column
df['Discount %'] = df['Discount %'].astype(str).str.replace('%','')
df['Discount %'] = pd.to_numeric(df['Discount %'], errors='coerce').fillna(0)

# Handle 'NA' region
df['Region'] = df['Region'].fillna('NA')

# Extract Year (optional for line chart)
df['Year'] = pd.to_datetime(df['Date']).dt.year

# Calculate data for charts
region_sales = df.groupby('Region')['Actual Price'].sum()
sales_trend = df.groupby('Year')['Actual Price'].sum()
avg_discount = df.groupby('Item')['Discount %'].mean()

# Create a single figure with 3 subplots
fig = plt.figure(figsize=(12,12))

# Bar chart (Sales by Region)
ax1 = fig.add_subplot(3,1,1)   # 3 rows, 1 column, first subplot
region_sales.plot(kind='bar', color='skyblue', edgecolor='black', ax=ax1)
ax1.set_title("Sales by Region")
ax1.set_ylabel("Total Sales")

# Line chart (Sales Trend)
ax2 = fig.add_subplot(3,1,2)
sales_trend.plot(kind='line', color='green', marker='o', ax=ax2)
ax2.set_title("Sales Trend Over Time")
ax2.set_ylabel("Total Sales")

# Pie chart (Average Discount by Product)
ax3 = fig.add_subplot(3,1,3)
avg_discount.plot(kind='pie', autopct='%1.1f%%', startangle=90, shadow=True, ax=ax3)
ax3.set_title("Average Discount by Product")
ax3.set_ylabel("")

plt.tight_layout()   # Adjust spacing
plt.show()
