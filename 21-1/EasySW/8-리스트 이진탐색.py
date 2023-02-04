import random
random.seed(777)
length=300
list=[]
for i in range(length):
    list.append(random.randint(0,1000))
list.sort() #오름차순 정렬
print(list)

#이진탐색으로 key값의 인덱스를 찾아낸다

key=559
index=0 #초기 인덱스값
counter=0 #탐색횟수 카운터

high=length
low=0
mid=(high+low)//2


while high>=low:
    counter+=1
    mid=(high+low)//2 #몫만 본다 int((high+low)/2)

    if list[mid]<key: #오른쪽 영역만 탐색
        low=mid+1 #하한값 갱신

    elif list[mid]>key: #왼쪽 영역만 탐색
        high=mid-1 #상한값 갱신

    elif list[mid]==key:
        index=mid
        break

print(f"{counter} binary searches found index {index}")
print(f"Key={key}, List[{index}]={list[index]}")

