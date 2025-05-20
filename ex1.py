import pandas as pd
import numpy as np

np.random.seed(0)
names = [f'Employee_{i}' for i in range(1, 51)]
ages = np.random.randint(22, 60, size=50)
departments = np.random.choice(['HR', 'Sales', 'IT', 'Marketing'], size=50)
salaries = np.random.randint(40000, 120000, size=50)

employee_df = pd.DataFrame({
    'Name': names,
    'Age': ages,
    'Department': departments,
    'Salary': salaries
})

print(employee_df.sort_values(by="Salary", ascending=True).tail(5))
print("********************************************")
print(employee_df[(employee_df["Department"]=="IT") &(employee_df["Salary"]>70000)])
print("********************************************")
print(employee_df["Department"].value_counts().sort_index())
print("********************************************")
# print(employee_df.sort_values(by=["Age", "Salary"], ascending=[False, True]))
print("*****************Bonus1***************************")
print(employee_df.groupby("Department")["Salary"].mean())
print("*****************Bonus2***************************")
marketing_df = employee_df[["Name", "Age"]][employee_df["Department"]=='Marketing']
youngest_index = marketing_df["Age"].idxmin()
print(marketing_df.loc[youngest_index, ["Name", "Age"]])
#           p rint(marketing_df[["Name", "Age"]]["Age"].idxmin())