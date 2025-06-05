import pandas as pd

df_rev_mar = pd.read_excel("excel_files/revenue_permon.xlsx", engine="openpyxl", sheet_name="4月")
print(df_rev_mar)
print(len(df_rev_mar))
line = 0
for line in range(len(df_rev_mar)):
    print(df_rev_mar.iloc[line, 5])
df_rev_may = pd.read_excel("excel_files/revenue_permon.xlsx", engine="openpyxl", sheet_name="5月")
df_rev_jun = pd.read_excel("excel_files/revenue_permon.xlsx", engine="openpyxl", sheet_name="6月")