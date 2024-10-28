import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r"https://raw.githubusercontent.com//ine-rmotr-curriculum//FreeCodeCamp-Pandas-Real-Life-Example//refs//heads//master//data//sales_data.csv")
print(data)
data['Revenue'] = data['Order_Quantity'] * data['Unit_Price']

# Convert 'date' to datetime format for time-based analysis
data['Date'] = pd.to_datetime(data['Date'])

# Group sales by Product, region, and customer segment
product_sales = data.groupby('Product')['Revenue'].sum()
region_sales = data.groupby('Country')['Revenue'].sum()
segment_sales = data.groupby('Customer_Gender')['Revenue'].sum()

# Analyze sales trends over time (e.g., daily revenue)
daily_sales = data.groupby('Date')['Revenue'].sum()



# Line Plot: Sales Trends Over Time
plt.figure(figsize=(10, 6))
plt.plot(daily_sales.index, daily_sales.values, marker='v', linestyle='-', color='teal')
plt.title('Sales Trends Over Time')
plt.xlabel('Date')
plt.ylabel('Total Revenue')
plt.grid(True)
plt.show()

# Area Chart: Cumulative Sales Over Time
cumulative_sales = daily_sales.cumsum()
plt.figure(figsize=(10, 6))
plt.fill_between(cumulative_sales.index, cumulative_sales.values, color='lightblue', alpha=0.5)
plt.title('Cumulative Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Cumulative Revenue')
plt.show()

# Bar Plot: Sales Performance by Product
plt.figure(figsize=(8, 4))
plt.bar(product_sales.index, product_sales.values, color='skyblue', edgecolor='black')
plt.title('Sales Performance by Product')
plt.xlabel('Product')
plt.ylabel('Total Revenue')
plt.legend(loc="upper left")
plt.show()

# Bar Plot: Sales Performance by Country
plt.figure(figsize=(8, 4))
plt.scatter( product_sales.index, product_sales.values, color='yellow', edgecolor='black', marker="x")
plt.title('Sales Performance by Country')
plt.xlabel('Country')
plt.ylabel('Total Revenue')
plt.legend(loc="upper right")
plt.show()

# Pie Chart: Distribution of Sales by Customer Segment
plt.figure(figsize=(8, 6))
plt.pie( 
    segment_sales.values,  # Data values for the pie chart
    labels=segment_sales.index, 
    autopct='%1.1f%%', 
    startangle=90, 
    colors=['lightgray', 'lightpink'], 
    wedgeprops={'edgecolor': 'black'}
)
plt.legend(loc="upper right")
plt.title('Sales Distribution by Customer Segment')
plt.ylabel('pie charts')  # Remove default ylabel for pie charts
plt.show()