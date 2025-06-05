import pandas as pd

df_rev_mar = pd.read_excel("excel_files/revenue_permon.xlsx", engine="openpyxl", sheet_name="4月")
print(df_rev_mar)
print(len(df_rev_mar))
line = 0
for line in range(len(df_rev_mar)):
    price = df_rev_mar.iloc[line, 5]
    num = df_rev_mar.iloc[line, 6]
    sum_price = price * num
    print(sum_price)
    line += 1
df_rev_may = pd.read_excel("excel_files/revenue_permon.xlsx", engine="openpyxl", sheet_name="5月")
df_rev_jun = pd.read_excel("excel_files/revenue_permon.xlsx", engine="openpyxl", sheet_name="6月")