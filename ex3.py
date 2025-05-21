import pandas as pd
import numpy as np

students = [f'Student_{i}' for i in range(1, 31)]
math_scores = np.random.randint(40, 100, size=30).astype(float)
english_scores = np.random.randint(40, 100, size=30).astype(float)

# Add some NaNs
math_scores[np.random.choice(30, 5, replace=False)] = np.nan
english_scores[np.random.choice(30, 3, replace=False)] = np.nan

student_df = pd.DataFrame({
    'Student': students,
    'Math': math_scores,
    'English': english_scores
})

# print(student_df)
print(student_df.isna().sum().sum())
print("***********************************")
print(student_df["Math"].fillna(student_df["Math"].mean()))
print(student_df["English"].fillna(student_df["English"].mean()))
print("***********************************")
student_df["Average"] = student_df.mean(axis=1, numeric_only=True)
print(student_df)
print("***********************************")
print(student_df[["Student", "Average"]][student_df["Average"]>80])

print("***************Bonus********************")
print(student_df[student_df["Math"].isna() & student_df["English"].isna() ])