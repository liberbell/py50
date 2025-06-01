import pandas as pd

df = pd.read_excel("excel_files/sell_list_new.xlsx", sheet_name="まとめ", header=2)
print(df)

df_renew =df.iloc[0:len(df)-2, 1:9].dropna()
df_name_unique = df_renew["担当者"].unique()

for name in df_name_unique:
    df_temp = df_renew[df_renew["担当者"] == name]
    
    print(df_temp)
    print(df_temp["売上金額"].sum())