# Set 연습
# Set은 대수학의 집합과 동일한 성질을 가진다
# 중복을 허용하지 않고, 순서가 없다(인덱싱 불가)
# 리스트 튜플에서 중복값 제거 위해 사용하기도 한다
print('')
s1 = {1,2,3,4}
s2 = set([1,2,3,4])  # 리스트의 자료형 변환

# .add()함수, .update()함수로 원소 추가, .remove()함수로 원소 제거
s1.add(6)  # 단일요소 추가
print(s1)
s1.update([1,2,3,4,99,999,999])  # 중복X, 리스트입력으로 다중요소 추가
print(s1)
s1.remove(99)
print(s1)

# 합집합, 교집합, 차집합, 대칭차집합
print('')
s2 = {77,777,1,2,3}
print(s1)
print(s2)
print(s1 & s2)  # 교집합
print(s1 | s2)  # 합집합
print(s1-s2)  # 차집합1
print(s2-s1)  # 차집합2
print((s1 | s2)-(s1 & s2))  # 대칭차집합(합집합에서 교집합부분만 제거) 괄호 필수!!

# .isubset(of집합), .isdisjoint(of집합) 부분집합, 교집합 여부 확인
print('')
s1 = {1,2,3,4,5,6,7}
s2 = {3,4,5}
print(s1.issubset(s2))  # s1이 s2의 부분집합인가? ㄴㄴ
print(s2.issubset(s1))  # s2가 s1의 부분집합인가? ㅇㅇ
print(s1.isdisjoint(s2))  # s1과 s2의 교집합이 없는가?
