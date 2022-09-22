#2022-09-22 자료형부터.. 공부 좀 하자

#1️⃣튜플 tuple 기호: ()
#리스트와 차이점 - 리스트는 변경 가능(새로운 리스트 추가 등) / 튜플은 변경 불가. 길이 및 값 등이 고정되어 있다.
t1 = (1, 2, 'a', 'b')
# del t1[0] #'tuple' object doesn't support item deletion
# t1[0] = c #'tuple' object doesn't support item deletion

print(t1[0])
print(t1[0:2])
#튜플 더하기
t2 = (3,4)
print(t1+t2)
#튜플 곱하기
print(t1*3)

#2️⃣딕셔너리 Dictionary ✨중요 기호: {}
#키-값의 형태 / API에서 자주 활용됨 
'''ex)JSON 
{
    "이름": "홍길동",
    "나이": "25",
    "성별: "여",
    "주소": "서울특별시 양천구 목동",
    "특기"["농구", "도술"],
    "가족관계: "{"#": 2, "아버지": 홍판서, "어머니": "춘섬"},
    "회사": "경기 수원시 팔달구 우만동"
 }'''

 #딕셔너리 = 연관배열(Associative array) or 해시(hash)
 #Key를 통해 Value를 얻는다.
dic = {"name": 'Eric', "age": 15}
print(dic['name'])
#딕셔너리 추가(key&value)
a = {1: 'a'}
a['name'] = "익명"
print(a)
#딕셔너리 삭제(key로 삭제)
del a[1]
print(a)
#딕셔너리 key이용하여 value 얻기
grade = {'pey': 10, 'julliet': 99}
print(grade['pey'])
print(grade['julliet'])
#딕셔너리 주의사항(key 중복 금지 / value는 같아도 됨)
a = {1: 'a', 1: 'b'}
print(a) #key가 중복될 경우, 마지막 key만 남는다
a = {1: 'a', 2: 'a'}
print(a)
#딕셔너리 Key리스트 만들기(Keys)
a = {1: '아이네', 2: '징버거', 3: '릴파'}
print(a.keys())
print(a.values()) #배열로 담을 수 있다.
print(a.items()) #새로운 배열 안에 튜플 형태로 담을 수 있다.
#for문으로 쓰는 경우
for k in a.keys(): #key만 뽑아서 반복문 돌리기
    print(k)

for v in a.values(): #value만 뽑아서 반복문 돌리기
    print(v)

for k, v in a.items():
    print("Key: "+str(k))
    print("Value: "+ v)

#딕셔너리 key: value 쌍 모두 지우기(clear)
# a.clear()
# print(a)
#get함수 사용(없는 key 확인 등을 할 때 사용)
#print(a[4]) #KeyError: 4
print(a.get(4)) #None / 4라는 key에 해당된 value가 없음을 확인
print(a.get(4, '없음')) # 찾는 값이 없을 때 뒤의 내용('없음')을 return하라
#(key) in (딕셔너리) / 해당 딕셔너리 안에 key를 찾을 때 사용
print(4 in a) #true 또는 false로 return함

#3️⃣집합 기호: set([]), {} / 다른 언어에서 구현 시 복잡
#집합은 중복된 요소를 가질 수 없다. / A: 1, 2, 5 B: 3, 4, 5 가능 / A: 1, 2, 2 B: 3, 4, 4 불가능
#집합 관련 처리를 위해 만들어진 자료형 / 중복을 허용하지 않는다 / 순서가 없다(Unordered)

#집합 정의(여러 방법이 있으니 참고할 것)
s1 = set([1, 2, 3]) #set=집합
s1 = {1,2,3}
print(s1)
print(type(s1))
#데이터 중복 시 활용 예제
l = [1,2,2,3,3] #list
newList = set(l) #list를 set(집합)으로 변환 / 중복값 제거
print(newList)
newList = list(set(l)) #set(집합)으로 변환한 값을 다시 list로 변환
print(newList)
#문자열의 중복도 제거한다 / 순서는 따로 없다
s2 = set("Hello")
print(s2)
#교집합(intersection)
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
print(s1 & s2)
print(s1.intersection(s2))
#합집합(union)
print(s1 | s2)
print(s1.union(s2))
#차집합(difference)
print(s1 - s2)
print(s1.difference(s2)) # s1 - s2
print(s2.difference(s1)) # s2 - s1
#집합에 하나의 값 추가(add)
s1.add(7)
print(s1)
#집합에 여러 값 추가(update)
s1.update([8,9,10])
s1.update([8,9,10,1]) #집합에 기존에 있는 중복값은 추가되지 않는다.
print(s1)
#집합에 하나의 특정 값 제거(remove)
s1.remove(10)
print(s1)
#집합에서 하나의 특정 값 제거(discard) / 집합에 제거하려는 값이 없어도 keyError를 발생시키지 않는다.
s1.discard(55) # s1 집합 안에 없는 값
print(s1)

#4️⃣불(bool) 논리형
#대문자로 시작해야한다. True / False
b1 = True
print(b1)
print(type(b1))
#Python의 bool 특징
# 값이 있는 경우(ex) "python" / [1,2,3]) = 참 / 값이 없는 경우(ex)"" / [](list) / ()(tuple) / {}(dictionary)) = 거짓
# 1 = 참 / 0 = 거짓 / None = 거짓

#예제
if b1:
    print(b1)
#예제2(104pg)
b2 = [1,2,3,4]
while b2: #조건이 True일 경우 무한 루프를 돌아야하지만 모든 값이 꺼내진 빈 list는 False로 인식되어 루프가 멈춘다. 
    b2.pop()
    print(b2)

#5️⃣변수
#자료형의 값을 저장하는 공간 / =(assignment) 사용
#파이썬에서 사용하는 변수는 객체를 가리키는 것
#변수(parameter)와 인수(arguement)의 차이: 변수(parameter) = 함수 선언의 변수 / 인수(arguement) = 함수로 보내는 실제 값, 실제 데이터

#list 변수 주의사항
# 변수에는 값이 아닌 값이 있는 곳의 주소가 저장된다(복사와 다른 개념)
a = [1, 2, 3]
b = a #a의 주소를 b에 넘긴 것(복사x)
a[1] = 4
print(a)
print(b)
#주소(id)
print(id(a))
print(id(b))
print(a is b) # 주소가 같은지 확인 / True 또는 False로 return
#복사(새롭게 만드는 것)
b = a[:] #a의 값을 slicing해서 b에 새롭게 만드는 것
a[1] = 5
print(a)
print(b) # b는 새로운 주소를 할당 받았기에 a에 영향을 받지 않는다.
print(id(a))
print(id(b)) #주소가 바뀌었다.
print(a is b) #False
#Copy모듈 활용
from copy import copy
b = copy(a) # a를 복사해서 b에 새롭게 할당
a[1] = 3
print(a)
print(b)
print(id(a))
print(id(b))
print(a is b)
#변수 할당하는 법
#tuple 자료형 / (a, b) = 'python', 'life' 과 동일한 결과
a, b = ('python', 'life')
print(a)
print(b)
#list 자료형 / tuple과 똑같이 작성해도 됨 / a, b = ['python', 'life'] / [a, b] = 'python', 'life'
[a, b] = ['python', 'life']
print(a)
print(b)
#String
a = b = "Hello"
print(a)
print(b)
#값 바꾸기(보편적 방법)
a = 3
b = 5
tmp = b
b = a
a = tmp
print(a)
print(b)
#값 바꾸기(Python 방법)
a = 2
b = 4
a,b = b,a #tuple활용?
print(a)
print(b)