import random
import time

ran="Y"

while ran=="Y":
    print("Rolling..")
    time.sleep(1)
    dic1=random.randint(1,6)
    dic2=random.randint(0,7)
    print(dic1,"   1 : 2  ",dic2)

    ran=input("Y an N   ")
