import pandas as pd
import numpy as np

products = ['Laptop', 'Smartphone', 'Tablet', 'Monitor']
regions = ['North', 'South', 'East', 'West']

sales_data = pd.DataFrame({
    'Product': np.random.choice(products, size=40),
    'Region': np.random.choice(regions, size=40),
    'Units_Sold': np.random.randint(5, 50, size=40),
    'Unit_Price': np.random.randint(200, 1500, size=40)
})
sales_data['Total_Sales'] = sales_data['Units_Sold'] * sales_data['Unit_Price']

print(sales_data.groupby('Product').agg({
    "Units_Sold": "sum",
    "Total_Sales": "sum"
}).reset_index())
print("**********************************************")
highest_avg = sales_data.groupby('Region')['Total_Sales'].mean().idxmax()
print(highest_avg)
sales_data['Sales tax(8%)'] = sales_data['Total_Sales'] + ( 0.08 * sales_data['Total_Sales'])
print(sales_data) 