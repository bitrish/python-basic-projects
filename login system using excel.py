import xlrd
import xlwt
from xlutils.copy import copy

loc1=r"C:\Users\HP\Desktop\python with risabh\studsheet.xls"
wrkbk=xlrd.open_workbook(loc1)
wrksht=wrkbk.sheet_by_name("Sheet1")
tonrow=wrksht.nrows
username=[]
password={}
for x in range(1,tonrow):
    username.append(wrksht.cell(x,0).value)
    password[username[x-1]]=str(wrksht.cell(x,1).value)

status="y"

def displayloginpg():
    status=input("Are yiu registered Y/N Q for quit")

    if status.lower()=="y":
        oldusr()
    if status.lower()=="n":
        newusr()

    if status.lower()=="q":
        exit()

def oldusr():
    print(username)
    print(password)
    print()

    lgnam=input("Enter user your name")
    pswrd=input("enter user your password")

    if password[lgnam]==pswrd:
        print("YOu are really registered in this system")
    else:
        print("password wrong or user not registered")

def newusr():
    newname=input("enter a unique username")
    newpass=input("enter a strong password")
    if newname in user:
        print("user name is already taken")
    else:
        user[newname]=newpass
        print("you have registered sucessfully")

while True:
    displayloginpg()
