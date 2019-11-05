import xlwt

wbk=xlwt.Workbook()
wst=wbk.add_sheet("sheet2")
wst.write(0,0,"Name")



font=xlwt.Font()
font.name= "Time New Roman"
font.colour_index=2
font.bold= True

style1=xlwt.XFStyle()
style1.font=font
style1.num_format_str="D-MMMM-YY"

from datetime import datetime
wst.write(1,0,datetime.now(),style1)
wst.write(2,0,1)
wst.write(2,1,1)
wst.write(2,2,xlwt.Formula("A3+B3"))

wbk.save("studsheet3.xls")
