import pandas as pd

df_history_mar = pd.read_csv("excel_files/history_mar.csv", encoding="shift-jis", engine="python")
df_history_may = pd.read_csv("excel_files/history_may.csv", encoding="shift-jis", engine="python")
print(df_history_mar)
print(df_history_may)