import pandas as pd

df_history1 = pd.read_csv("excel_files/history_mar.csv", encoding="shift-jis", engine="python")
print(df_history1)

df_division = pd.read_excel("excel_files/division_list.xlsx", engine="openpyxl", sheet_name="Sheet1")
print(df_division)

df_merge = pd.merge(df_history1, df_division, on="社員番号")
df_merge = df_merge.iloc[:, [0, 1, 2, 9, 3, 4, 5, 6, 7]].sort_values("ID")

df_merge2 = pd.merge(df_history1, df_division, left_on="担当者", right_on="名前")
df_merge2 = df_merge2.iloc[:, [0, 1, 2, 9, 3, 4, 5, 6, 7]].sort_values("ID")

# df_merge.to_excel("excel_files/merge_history_division.xlsx", index=False)
# df_merge.to_csv("excel_files/merge_history_division.csv", index=False, encoding="shift-jis")

df_merge2.to_excel("excel_files/merge_history_division2.xlsx", index=False)
df_merge2.to_csv("excel_files/merge_history_division2.csv", index=False, encoding="shift-jis")