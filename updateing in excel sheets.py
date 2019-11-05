
import xlrd
import xlwt
from xlutils.copy import copy

loc1=r"C:\Users\HP\Desktop\python with risabh\studsheet.xls"
loc2=r"C:\Users\HP\Desktop\python with risabh\studsheet.xls"
rb=xlrd.open_workbook(loc1)

wb=copy(rb)

wsheet=wb.get_sheet(0)

wsheet.write(0,0,"NMI")

wb.save(loc2)
