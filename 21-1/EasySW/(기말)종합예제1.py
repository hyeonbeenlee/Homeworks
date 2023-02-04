import random as rd
import math
import os

filepath='./문제지.txt'
outf=open(filepath,'w')

score=0
probnum=1
syms=['+','-','*','/']
name=input('이름: ')
nameinfo=f"이름 : {name}\n"
outf.write(nameinfo)

while probnum<=5:
    num1=rd.randint(1,10)
    num2=rd.randint(1,10)
    sym=rd.choice(syms)
    print(f"문제{probnum}) {num1} {sym} {num2} = ",end='')
    if sym=='+':
        ans=num1+num2
    elif sym=='-':
        ans=num1-num2
    elif sym=='*':
        ans=num1*num2
    elif sym=='/':
        ans=math.floor(num1/num2)
    stu_ans=int(input(''))
    if stu_ans==ans:
        score+=1
        print(f'정답! 현재 {score}점')
    else:
        print('오답이예요깔깔')

    save=f"{num1} {sym} {num2} = {stu_ans}\n"
    outf.write(save)
    probnum += 1

print(f"{score}/{probnum-1} 점!")