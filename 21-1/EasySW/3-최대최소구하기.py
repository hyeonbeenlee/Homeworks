a=input()
b=input()
c=input()
d=0
#총 6가지 경우의 수에 대해 정의해줘야한다
if a>b:
    if b>c: #a>b>c
        max=a
        min=c
    else: #a>b, c>b
        if a>c: #a>c>b
            max=a
            min=c
        else: #c>a>b
            max=c
            min=b
else: #b>a
    if a>c: #b>a>c
        max=b
        min=c
    else: #b>a, c>a
        if b>c: #b>c>a
            max=b
            min=a
        else: #c>b>a
            max=c
            min=a


print(max)
print(min)