#immutable(변하지 않는 자료형) #java의 call by value
#정수, 실수, 문자열, 튜플
a = 1
def vartest(a):
    a = a + 1

vartest(a)
print(a)

#mutable(변할 수 있는 자료형) #java의 call by reference
#리스트, 딕셔너리, 집합
b = [1,2,3] #전역변수
def vartest2(b): #전역변수의 주소를 넘겨주는 것? 애매하네..
    b = b.append(4) #지역변수?
#전역변수 b와 지역변수 b는 이름만 같고 실제로는 다른 변수이다. 전역변수가 변화 가능한 자료형이기에 변화하였다.
vartest2(b)
print(b)

#immutable은 지역변수를 별도로 전역변수(global) 선언을 해주어야 수정할 수 있다.
