class Calc:
    __num1=0
    __num2=0
    __result=0

    def __init__(self,num1,num2):
        self.__num1=num1
        self.__num2=num2

    def changenum(self,num1,num2):
        self.__num1=num1
        self.__num2=num2

    def add(self):
        self.__result=self.__num1+self.__num2
        print(self.__result)

    def subtract(self):
        self.__result=self.__num1-self.__num2
        print(self.__result)

    def multiply(self):
        self.__result=self.__num1*self.__num2
        print(self.__result)

    def divide(self):
        if self.__num2==0:
            self.__result='NaN'
            print('Cannot divide by 0, NaN')
        else:
            self.__result=self.__num1/self.__num2
            print(self.__result)


a=input('Num 1: ')
b=input('Num 2: ')
a=int(a);   b=int(b);
X=Calc(a,b)

while True:
    print('\n1. Add')
    print('2. Subtract')
    print('3. Multiply')
    print('4. Divide')
    print('5. Change numbers')
    calc=input('')
    if calc==str(1):
        X.add()
    elif calc==str(2):
        X.subtract()
    elif calc==str(3):
        X.multiply()
    elif calc==str(4):
        X.divide()
    elif calc==str(5):
        newnum1=int(input('Num1 : '))
        newnum2=int(input('Num2 : '))
        X=Calc(newnum1,newnum2)
    else:
        print('Bye!')
        break
