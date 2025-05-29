import pandas as pd

df = pd.read_excel("excel_files/sell_list.xlsx", sheet_name="Sheet1")

print(df["売上金額"])
print(df["売上金額"].mean())
print(df["売上金額"].sum())
print(df["売上金額"].min())
print(df["売上金額"].max())

print(df[["担当者", "売上金額"]])

print(df.iloc[2, 3])