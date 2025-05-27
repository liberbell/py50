import openpyxl

wb = openpyxl.load_workbook("excel/bill_list.xlsx")
ws = wb["Sheet1"]

wb_test1 = openpyxl.load_workbook("excel/bill_test1.xlsx")
ws_test1 = wb_test1["Sheet1"]
print(ws_test1.cell(row=4, column=7).value)
print(ws_test1.cell(3, 14).value)

wb_test2 = openpyxl.load_workbook("excel/bill_test2.xlsx")
ws_test2 = wb_test2.worksheets[0]
print(ws_test2.cell(4, 7).value)

wb_test3 = openpyxl.load_workbook("excel/bill_test3.xlsx")
ws_test3 = wb_test3.worksheets[0]

ws_cell = ws_test1.cell(3, 14).value
wb.save("excel/bill_list.xlsx")