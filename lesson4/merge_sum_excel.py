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

df_merge_employee = pd.merge(df_concat, df_employee, on="社員番号")
df_merge_employee = df_merge_employee.iloc[:, [0, 1, 2, 3, 8, 4, 5, 6, 7]]
print(df_merge_employee)

df_name_list = df_merge_employee["名前"].unique()
print(df_name_list)
for name in df_name_list:
    df_divide_employee = df_merge_employee[df_merge_employee["名前"] == name]
    df_pivot = df_divide_employee.pivot_table(index="取引先", columns="商品名", values="売上金額", aggfunc="sum", fill_value=0, margins=True)
    print(df_divide_employee)
    print(df_pivot)

