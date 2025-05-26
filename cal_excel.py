import openpyxl

wb = openpyxl.load_workbook("excel/bill_list.xlsx")
ws = wb["Sheet1"]