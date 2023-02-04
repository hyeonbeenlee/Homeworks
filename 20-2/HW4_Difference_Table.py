import numpy as np
def datainput(n,storage): #n개 데이터포인트를 storage에 입력받는 함수
    for i in range(0,n,1):
        #globals()['vy{}'.format(i)]=float(input('Enter Y{} : '.format(i))) #동적 변수명 할당방식
        x=float(input('Enter X{} : '.format(i)))
        storage[0,i]=x #1행에 x값 저장

    for i in range(0,n,1):
        # globals()['vy{}'.format(i)]=float(input('Enter Y{} : '.format(i))) #동적 변수명 할당방식
        y=float(input('Enter Y{} : '.format(i)))
        storage[1,i]=y  #2행에 y값 저장

def diff(n,storage): #차분계산
    for i in range(1,n,1): #차수에 대한 반복 i=1,2....n-1
        for j in range(0,n-1,1): #데이터수에 대한 반복 j=0,1,2....n-2
            storage[i+1,j]=storage[i,j+1]-storage[i,j]
            #storage배열 [2,0] [2,1] [2,2]...에 ([1,1]-[1,0), ([1,2]-[1,1])....([1,n-1]-[1,n-2])를 할당

def divdiff(n,storage): #분할차분계산
    for i in range(1,n,1): #차수에 대한 반복 i=1,2....n-1
        for j in range(0,n-1,1): #데이터수에 대한 반복 j=0,1,2....n-2
            storage[i+1,j]=(storage[i,j+1]-storage[i,j])/(storage[0,j+i]-storage[0,j])
            #1차 : x1-x0, x2-x1, x3-x2
            #2차 : x2-x0, x3-x1
            #3차 : x3-x0

ndata=int(input('Number of data points? : '))
storage=np.zeros((10,10))
datainput(ndata,storage)

print('X Datas : {}'.format(storage[0,0:ndata]))
print('Y Datas : {}'.format(storage[1,0:ndata]))

diff(ndata,storage)
for i in range(ndata-1):
    print('{} order differences : {}'.format(i+1,storage[i+2,0:ndata-(i+1)]))

divdiff(ndata,storage)
for i in range(ndata-1):
    print('{} order divided differences : {}'.format(i+1,storage[i+2,0:ndata-(i+1)]))

print('Stored array is : \n{}'.format(storage))

