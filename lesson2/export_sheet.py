import pandas as pd

df = pd.read_excel("excel_files/sell_list_new.xlsx", sheet_name="まとめ", header=2)
print(df)

df_renew =df.iloc[0:len(df)-2, 1:9]
print(df_renew)