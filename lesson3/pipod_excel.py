import pandas as pd

df_history_mar = pd.read_csv("excel_files/history_mar.csv", encoding="shift-jis", engine="python")
df_pivot = df_history_mar.pivot_table(index="担当者", columns="取引先", values="対応工数(h)", aggfunc="sum")
print(df_pivot)

df_pivot = df_history_mar.pivot_table(index="担当者", columns=["取引先", "カテゴリ"], values="対応工数(h)", aggfunc="sum")
print(df_pivot)