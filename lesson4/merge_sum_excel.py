import pandas as pd

month_list = ["4月", "5月", "6月"]
sheet_name = pd.ExcelFile("excel_files/revenue_permon.xlsx").sheet_names

df_concat = pd.DataFrame()

for month in sheet_name:
    df_month = pd.read_excel("excel_files/revenue_permon.xlsx", engine="openpyxl", sheet_name=month)
    df_concat = pd.concat([df_concat, df_month])

df_concat["売上金額"] = df_concat["単価"] * df_concat["個数"]

df_employee = pd.read_excel("excel_files/employee_list.xlsx")
# df_employee["社員番号"] = df_employee["社員番号"].str.replace("A-", "")
df_employee["社員番号"] = df_employee["社員番号"].str.replace("[A-Z]-", "", regex=True)
df_employee = df_employee.astype({"社員番号":int})
print(df_employee)
print(df_concat)

df_merge_employee = pd.merge(df_concat, df_employee, on="社員番号")
print(df_merge_employee)