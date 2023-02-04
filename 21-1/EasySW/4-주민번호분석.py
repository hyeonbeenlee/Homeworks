# jumin=input() #123456-1234567
# front=jumin.split('-')[0]
# back=jumin.split('-')[1]
# year='19'+front[:2] if int(front[:2])>10 else '20'+front[:2]
# month=int(front[2:4]) #2,3
# date=int(front[4:]) #4,5
# gender='남성' if int(back[0])==1 or 3 else '여성'
#
# print(jumin)
# print(f"{year}년{month:02d}월{date:02d}일생 {gender}")

num=int(input())
factorial=1

for i in range(1,num+1,1):
    factorial*=i #팩토리얼 계산

str_factorial=str(factorial) #문자형으로 변환
numbers=[]

for i in range(len(str_factorial)):
    numbers.append(int(str_factorial[i])) #문자형 변환 팩토리얼 자릿수값을 1개씩 리스트에 저장, 저장 시 다시 정수형 변환

sum=0
for i in range(len(numbers)):
    sum+=numbers[i] #자릿수를 더함
print(sum)