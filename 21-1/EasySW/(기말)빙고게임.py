import numpy as np

nums = []
for i in range(1,26,1):
    nums.append(i)
bingolist = np.reshape(nums,(5,5)).tolist()

run=True
get=[]



while run:
    #매 입력마다 카운터 초기화
    rowcount = 0
    colcount = 0
    Rdiagcount = 0
    Ldiagcount = 0

    num=int(input())

    #범위 초과시
    if num<1 or num>25:
        print('범위 초과')
        continue

    get.append(num)
    #중복 시 요소제거 후 되돌아감
    if get.count(num)>=2:
        get.pop()
        print('중복')
        continue

    #입력된 빙고리스트 요소 0으로 만듬
    for i in range(len(bingolist)):
        for j in range(len(bingolist[i])):
            if num==bingolist[i][j]:
                bingolist[i][j]=0


    for i in range(5):
        for j in range(5):
            #행 체크
            if bingolist[i][j]==0:
                rowcount+=1
            #열 체크
            if bingolist[j][i]==0:
                colcount+=1

        if rowcount==5 or colcount==5:
            run=False
            break #i for문 탈출

        #오른대각선
        if bingolist[i][i]==0:
            Rdiagcount+=1
        #왼대각선
        if bingolist[i][4-i]==0:
            Ldiagcount+=1


    if Rdiagcount==5 or Ldiagcount==5:
        run=False


if run==False:
    print('Bingo')