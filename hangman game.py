import random

ans=['patt','hatt','ratt']
print(ans)
random.shuffle(ans)

wrd=ans[0];
print(wrd)

wrd=list(wrd)
print(wrd)


li=[]
for i in range(len(wrd)):
    li.append('_')

while 'true':
    print(' '.join(li))
    letter=input("enter the letter")

    if letter in wrd:
        for i in range(len(wrd)):
            if letter==wrd[i] and li[i]=='_':
                break

        li[i]=wrd[i]

        if ''.join(li)==''.join(wrd):
            break

print("You found it:  ", (li))
