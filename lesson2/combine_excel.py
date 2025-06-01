from glob import glob
import pandas as pd

files = glob("excel_files/revenue_*.xlsx")

df_tanaka = pd.read_excel(files[0], sheet_name="Sheet1")
df_sato = pd.read_excel(files[1], sheet_name="Sheet1")

df_concat = pd.concat([df_tanaka, df_sato], ignore_index=True)