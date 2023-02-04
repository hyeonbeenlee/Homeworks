# 다이아몬드 하짱
n=15
for i in range(n):
    print(f"{'*'*i:>{n}s}{'*'*i:<{n}s}")
print('************★하게★************')
for i in range(n-1,0,-1):
    print(f"{'*' * i:>{n}s}{'*' * i:<{n}s}")
