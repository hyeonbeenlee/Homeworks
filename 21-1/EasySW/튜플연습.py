t=(1,(1,2),(1,2,3))

#1
#1 2
#1 2 3 으로 출력되게 하라

for i in t:
    if type(i)==tuple:
        for j in i:
            print(f"{j:3d}",end=' ')
        print('')

    else: print(f"{i:3d}")

#변수선언 바꿔치기A
print('')
num1=1
num2=2
num2,num1=num1,num2
print(num1, num2)

#튜플로 변수선언
print('')
(a,(b,c),(d,e,f))=t
print(a,b,c,d,e,f)

#인덱싱
print('')
t=(1,2,3,4,5,6,7,8,9)
print(t[3:])
print(t[3:5]) #t[3], t[4]
print(t[:-1]) #t[-1]=9이므로 8까지 출력
print(t[-3:-1]) #t[-3], t[-2]
print(t[-0]) #t[0]

#덧셈과 곱셈
print('')
t1=(1,2,3); t2=(4,5,6);
print(t1+t2)
print(3*t1)

#count함수와 index함수
print('')
t=(1,1,1,3,3,4)
print(t.count(1))
print(t.index(1)) #첫번째 요소 인덱스 반환
print(t.index(4))