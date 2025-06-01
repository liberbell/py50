from glob import glob
import pandas as pd

files = glob("excel_files/revenue_*.xlsx")

df_concat = pd.DataFrame()

for file in files:
    df_temp = pd.read_excel(file, sheet_name="Sheet1")
    df_concat = pd.concat([df_concat, df_temp])

df_concat.to_excel("excel_files/revenue_all.xlsx", index=False)
