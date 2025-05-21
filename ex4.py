import pandas as pd
import numpy as np

customers = [f'Customer_{i}' for i in range(1, 21)]
emails = [f'customer{i}@example.com' for i in range(1, 21)]
order_ids = [f'ORD{i:04}' for i in range(1, 21)]
order_status = np.random.choice(['Shipped', 'Pending', 'Cancelled'], size=20)
order_values = np.random.randint(100, 1000, size=20)

orders_df = pd.DataFrame({
    'Customer': customers,
    'Email': emails,
    'Order_ID': order_ids,
    'Status': order_status,
    'Order_Value': order_values
})

print(orders_df[orders_df["Status"]=="Shipped"])
print("********************************************")
average = orders_df["Order_Value"].mean()
print("Average: ", average)
print(orders_df[orders_df["Order_Value"]>average])
print("********************************************")
print(orders_df['Email'].str.split('@'))
print("********************************************")
status_df = orders_df.groupby('Status')['Customer'].count()
print(status_df)