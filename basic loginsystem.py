user={}
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
    lgnam=input("Enter user your name")
    pswrd=input("enter user your password")

    if lgnam in user and user[lgnam]==pswrd:
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
