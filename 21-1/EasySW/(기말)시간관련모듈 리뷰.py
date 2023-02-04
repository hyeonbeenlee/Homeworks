import datetime as dt
import time

a=dt.datetime.now()
print(a)
print(f"{a.year}년 {a.month}월 {a.day}일 {a.hour}시 {a.minute}분 {a.second}초")

print('5초 뒤에 출력')
time.sleep(5)

a=dt.datetime.now()
print(a)
print(f"{a.year}년 {a.month}월 {a.day}일 {a.hour}시 {a.minute}분 {a.second}초")