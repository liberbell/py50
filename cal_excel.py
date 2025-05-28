import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.styles.borders import Border, Side
from glob import glob

wb2 = openpyxl.Workbook()
ws2 = wb2.active
ws2_title = "Sheet1"

headers = ["Bill Number", "Bill Name", "Amount", "Date"]
columns = ["A", "B", "C", "D"]
side = Side(style="thin", color="000000")
border = Border(left=side, bottom=side, right=side, top=side)

for i in range(len(headers)):
    ws2.cell(1, i + 1).value = headers[i]
    ws2.cell(1, i + 1).font = Font(bold=True)
    ws2.cell(1, i + 1).fill = PatternFill("solid", fgColor="FFA500")
    ws2.cell(1, i + 1).alignment = Alignment(horizontal="centerContinuous")
    ws2.cell(1, i + 1).border = border

files = sorted(glob("excel/bill_test*.xlsx"))

for file in files:

    wb_test = openpyxl.load_workbook(file, data_only=True)
    ws_test = wb_test.worksheets[0]

    line = ws.max_row + 1
    ws2.cell(line, 1).value = ws_test.cell(3, 14).value
    ws2.cell(line, 2).value = ws_test.cell(3, 1).value
    ws2.cell(line, 3).number_format = r"¥#,##0;¥-#,##0"
    ws2.cell(line, 3).value = ws_test.cell(15, 4).value
    ws2.cell(line, 4).number_format = r"yyyy/m/d"
    ws2.cell(line, 4).value = ws_test.cell(4, 14).value

wb2.save("excel/bill_list_orginal.xlsx")