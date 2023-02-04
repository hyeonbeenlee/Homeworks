import random
goal=random.randint(1,11)
cnt=1
while cnt<4:
    a=int(input('Guess : '))
    if a>goal:
        print('down')
    elif a<goal:
        print('up')
    elif a==goal:
        break
    cnt+=1

if a==goal:
    print('success')
else:
    print('fail')