import openpyxl

wb = openpyxl.load_workbook("excel/bill_list.xlsx")
ws = wb["Sheet1"]

wb_test1 = openpyxl.load_workbook("excel/bill_test1.xlsx")
ws_test1 = wb_test1["Sheet1"]

wb_test2 = openpyxl.load_workbook("excel/bill_test2.xlsx")
ws_test2 = wb_test2["Sheet1"]

wb_test3 = openpyxl.load_workbook("excel/bill_test3.xlsx")
ws_test3 = wb_test3["Sheet1"]