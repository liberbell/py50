import pandas as pd

df_history1 = pd.read_csv("excel_files/history_mar.csv", encoding="shift-jis", engine="python")
print(df_history1)

df_division = pd.read_csv("excel_files/division_list.csv", encoding="shift-jis" engine="python")
print(df_division)