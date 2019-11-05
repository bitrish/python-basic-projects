import xlrd

loc=r"C:\Users\HP\Desktop\python with risabh/studsheet.xlsx"
workbook=xlrd.open_workbook(loc)
worksheet=workbook.sheet_by_name("Sheet1")

print("Value at column 4 row 2 : {0}".format(worksheet.cell(0,0).value))

noofsheets=workbook.nsheets
print(noofsheets)

nameofsheets=workbook.sheet_names()
print(nameofsheets)

tnor=worksheet.nrows
print(tnor)

tnoc=worksheet.ncols
print(tnoc)

record=list()
table=list()

for x in range(tnor):
    for y in range(tnoc):
        record.append(worksheet.cell(x,y).value)
    table.append(record)
    record=[]

print(table)
