class human:
    __name = ''
    __age = 0
    __gender = None
    __count = 0

    # 클래스 메소드로 생성된 객체는 모든 클래스 내 객체가 공유함
    @classmethod
    def inccount(cls):
        cls.__count += 1

    @classmethod
    def deccount(cls):
        cls.__count -= 1

    @classmethod
    def getcount(cls):
        return cls.__count

    # 은닉된 객체 메소드또한 외부에서 접근 불가
    def __gender2tr(self):
        if self.__gender == 1:
            return '존예녀'
        if self.__gender == 2:
            return '한남'
        else:
            return '제3의성'

    # 객체 생성자, 객체가 생성될 때 마다 호출됨
    def __init__(self,name,age,gender):
        self.__name = name
        self.__age = age
        self.__gender = gender
        human.inccount()  # 클래스 메소드를 호출(객체 생성 시 마다 카운트를 증가)

    def getname(self):
        return self.__name

    def getage(self):
        return self.__age

    def getgender(self):
        return self.__gender

    # 클래스 내부에서는 은닉된 메소드 접근 가능
    def setname(self,name):
        self.__name = name

    def setage(self,age):
        self.__age = age

    def setgender(self,gender):
        self.__gender = gender

    def view(self):
        print(f"이름은 {self.__name} {self.__age}세 {self.__gender2tr()}")

    # 객체 소멸자, 객체가 메모리에서 사라질 때 수행됨
    def __del__(self):
        human.deccount()


humanlist = []


def menuView():
    print('*' * 30)
    print(f"{'1. 추가':^30s}")
    print(f"{'2. 삭제':^30s}")
    print(f"{'3. 전체출력':^30s}")
    print(f"{'Q. 종료':^30s}")
    print('*' * 30)


def humanAdd():
    inStr = input('이름 나이 성별(1/2/else) 을 입력하세요: ')
    inStr=inStr.split()
    name = inStr[0]
    age = int(inStr[1])
    gender = int(inStr[2])
    h = human(name,age,gender)
    humanlist.append(h)  # 리스트에 객체 저장됨


def humanDel():
    allView()
    inName = input('삭제할 사람 이름을 입력하세요: ')
    isFind = False  # 삭제할 사람이 리스트에 있는가?
    for i in range(len(humanlist)):
        if inName == humanlist[i].getname():
            isFind = True
            break
    if isFind == True:
        del humanlist[i]  # break 후 for루프의 마지막 변수가 할당된다
    else:
        print('찾을 수 없습니다')


def allView():
    print()
    print('*' * 30)
    for i in range(len(humanlist)):
        humanlist[i].view()
    print('*' * 30)
    print()


while True:
    menuView()
    choice = input()

    if choice == '1':
        humanAdd()

    elif choice == '2':
        humanDel()

    elif choice == '3':
        allView()

    elif choice == 'Q':
        break

    else:
        print('똑바로 해라\n')
