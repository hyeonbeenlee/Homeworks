def calc(op,num1,num2):
    if op == '+':
        return num1+num2
    elif op == '-':
        return num1-num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        return num1 / num2  # 0으로 나누는 예외처리는 따로 안함

print(calc('*',2,3))