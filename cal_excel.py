import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.styles.borders import Border, Side
from glob import glob

wb = openpyxl.load_workbook("excel/bill_list.xlsx")
ws = wb["Sheet1"]

wb_test1 = openpyxl.load_workbook("excel/bill_test1.xlsx", data_only=True)
ws_test1 = wb_test1["Sheet1"]

files = sorted(glob("excel/bill_test*.xlsx"))

for file in files:

    wb_test = openpyxl.load_workbook(file, data_only=True)
    ws_test = wb_test.worksheets[0]

    line = ws.max_row + 1
    ws.cell(line, 1).value = ws_test.cell(3, 14).value
    ws.cell(line, 2).value = ws_test.cell(3, 1).value
    ws.cell(line, 3).number_format = r"¥#,##0;¥-#,##0"
    ws.cell(line, 3).value = ws_test.cell(15, 4).value
    ws.cell(line, 4).number_format = r"yyyy/m/d"
    ws.cell(line, 4).value = ws_test.cell(4, 14).value

wb.save("excel/bill_list.xlsx")