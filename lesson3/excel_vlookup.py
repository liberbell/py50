import pandas as pd

df_history1 = pd.read_csv("excel_files/history_mar.csv", encoding="shift-jis", engine="python")
print(df_history1)

df_division = pd.read_excel("excel_files/division_list.xlsx", engine="openpyxl", sheet_name="Sheet1")
print(df_division)