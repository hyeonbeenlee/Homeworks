# 1 1 1 4 5 6 3 을
# 1 3 4 5 6 으로 출력
# 중복된 값 제거, 오름차순 sort

instr = input()  # 1 2 3 띄워서 입력하면
chars = instr.split()  # ['1','2','3'] 구분해 저장함
print(chars)
for i in range(len(chars)):
    chars[i] = int(chars[i])  # 정수형으로 변환
print(chars)

chars = set(chars)  # 집합으로 변경, 중복제거
print(chars)

chars = list(chars)
chars.sort()

for i in range(len(chars)):
    print(chars[i],end=' ')
