import random
import time

ran="Y"

while ran=="Y":
    print("Rolling..")
    time.sleep(1)
    dic1=random.choice([4,6,5,8,1])
    dic2=random.randrange(0,7,2)
    dic3=random.random()

    li=[6,5,2]
    dis6=random.shuffle(li)
    print(li[0])
    print(li[1], "  ",li[2])
    dic7=random.uniform(1,10)
    random.seed(0)
    dic4=random.random()
    random.seed(0)
    dic5=random.random()

    print(dic1,"  ",dic2, "  ",dic3, "  ",dic4," ",dic5," ",dic7)

    ran=input("Y an N   ")
