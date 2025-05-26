import openpyxl

wb = openpyxl.load_workbook("excel/bill_list.xlsx")
ws = wb["Sheet1"]

wb_test1 = openpyxl.load_workbook("excel/bill_test1.xlsx")
ws_test1 = wb_test1["Sheet1"]