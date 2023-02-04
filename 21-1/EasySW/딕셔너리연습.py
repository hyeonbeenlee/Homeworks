#기본 연습
d={1:100,2:200,3:300,4:6974}
print(len(d)) #길이
d[5]=6969 #새로운 key에 value할당
print(d)
del d[3] #딕셔너리 요소 제거
print(d)
print(d[2]) #인덱싱

#.keys()함수, .values()함수, .items()함수
print('')
d={'key1':1, 'key2':2, 'key3':3}
print(d.keys()) #키값 리스트
print(d.values()) #밸류 리스트
print(d.items()) #[(키,밸류),(키,밸류)...] 리스트

#in 으로 key확인, .clear()함수
print('')
print('key1' in d) #key가 항상 우선이다
print('key9' in d)
d.clear() #내용 비움
print(d)



