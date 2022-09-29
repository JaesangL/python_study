#Class(클래스)
#반복되는 변수&메서드(함수)를 미리 정해놓은 틀(설계도)
#class명은 처음에 대문자로 쓰는게 정석
class Calculator:
    def __init__(self): #처음 클래스를 만들 때 어떤 값을 설정할지 정하는 것. 클래스를 사용할 때 무조건 처음 실행되는 함수 / 일종의 생성자
        self.result = 0
    def add(self, num):
        self.result +=num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))

#계산기 만들기
class FourCal:
    def setdata(self, first, second): #self는 객체를 담는 것 / 여기서는 a가 self로 들어간다.
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result

a = FourCal()
a.setdata(1,2)
print(a.first)
print(a.second)
print(a.add())

#__init__ 사용하기
class FourCal2:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second): #__init__과 동일한 기능이나 setdata는 따로 호출을 해주어야 동작한다.
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

#b = FourCal2() 
#TypeError: FourCal2.__init__() missing 2 required positional arguments: 'first' and 'second'
#b라는 객체를 만들기 위해 FourCal2()를 실행하면 __init__이 실행되기 때문에 first, second 인수가 없어서 오류가 발생한다.
b = FourCal2(1,2)

#클래스 상속
class MoreFourCal(FourCal2):
    def pow(self): #부모의 __init__이 있기에 굳이 안써줘도 될듯
        result = self.first ** self.second
        return result

a = MoreFourCal(4,2)
print(a.add())
print(a.pow())

#자식 클래스 변형 / 메서드 오버라이딩(method overiding)
class SafeFourCal(FourCal2): #자식 클래스가 부모 클래스보다 우선시 된다.
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second

a = SafeFourCal(4,0)
b = FourCal2(4, 0)
print(a.div())
#print(b.div()) #ZeroDivisionError: division by zero

#클래스 변수, 객체 변수
#클래스 변수란 클래스 안에 정의된 변수
class Family:
    lastname = "김"

Family.lastname = "박" #클래스 함수 바꾸기
print(Family.lastname)

a = Family()
b = Family()

print(a.lastname)
print(b.lastname)