import xlrd

workbook=xlrd.open_workbook("studsheet.xlsx")
worksheet=workbook.sheet_by_name("Sheet1")

print("Value at column 4 row 2 : {0}".format(worksheet.cell(0,0).value))
