import pandas as pd

df = pd.read_excel("excel_files/sell_list.xlsx", sheet_name="Sheet1")
print(df)

print(df[df["担当者"] == "田中"])

print(df[df["売上金額"] > 300000])

print(df[(df["担当者"] == "田中") & (df["売上金額"] > 300000)])

print(df[(df["担当者"] == "田中") | (df["売上金額"] >= 300000)].reset_index(drop=True))

print(df[(df["担当者"] == "田中") | (df["売上金額"] >= 300000)].iloc[40, 3])