class human:
    __name = ''
    __age = 0
    __gender = None
    __count = 0

    # 클래스 메소드로 생성된 메소드(함수)는 모든 클래스 내 메소드 내에서 사용할 수 있음
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
        if self.__gender == 0:
            return '존예녀'
        if self.__gender == 1:
            return '한남'
        else:
            return '제3의성'

    # 객체 생성자, 객체가 생성될 때 마다 호출됨
    def __init__(self,name,age,gender):
        self.__name = name
        self.__age = age
        self.__gender = gender
        human.inccount() #클래스 메소드를 호출(객체 생성 시 마다 카운트를 증가)

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

print(human.getcount())
h1 = human('김하경',25,0)
h1.view()
print(human.getcount())
h2 = human('이대우',57,3)  # 매력적인 중년 남자친구 없으므로 가림
h2.view()
print(human.getcount())
h3 = human('이현빈',26,1)
h3.view()
print(human.getcount())
del h2
print(human.getcount()) # 이대우 제거당함




# # h1 (a.k.a.김하경게이놈) 의 대변신은...
# h1.setname('하경공주')  # 히메사마
# h1.setage(17)  # 여고생쟝
# h1.setgender(0)  # 존예녀
# # print("Few minutes later.......\n그의 대 변 신!")
# h1.view()

# # 은닉된 메소드는 외부에서 접근할 수 없다
# print(h1.__name)
