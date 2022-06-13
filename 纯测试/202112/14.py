from openpyxl import Workbook
wb = Workbook()
ws = wb.worksheets[0]
row = ["a","b","c","d","e","f"]
ws.append(row)
wb.save("./hello.xlsx")