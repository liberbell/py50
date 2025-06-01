import pandas as pd

df = pd.read_excel("excel_files/sell_list.xlsx", sheet_name="Sheet1")
print(df)

print(df[df["担当者"] == "田中"])

print(df[df["売上金額"] > 300000])

print(df[(df["担当者"] == "田中") & (df["売上金額"] > 300000)])

print(df[(df["担当者"] == "田中") | (df["売上金額"] >= 300000)].reset_index(drop=True))

print(df[(df["担当者"] == "田中") | (df["売上金額"] >= 300000)].iloc[40, 3])

df_tanaka = df[df["担当者"] == "田中"].reset_index(drop=True)
print(df_tanaka)
df_tanaka.to_excel("excel_files/revenue_tanaka.xlsx", index=False)

df_nakamura = df[df["担当者"] == "中村"].reset_index(drop=True)
print(df_nakamura)

df_suzuki = df[df["担当者"] == "鈴木"].reset_index(drop=True)
print(df_suzuki)