# # 함수(function) / 함수 정의(definition), 호출(call)
# #구조 def 함수명(매개변수):
# #           <수행할 문장1>
# #           <수행할 문장2>
# #           ...
# #           return 리턴값

# #함수 정의(definition)
def sum(a, b):
    result = a + b
    return result
#함수 호출(call)
print(sum(1,2))

#1️⃣입력값(input)이 없는 경우
def say():
    return "Hi"
print(say())

#2️⃣결과값(output)이 없는 경우 / 들여쓰기 주의, % 뒤에 한 개 이상의 변수가 있는경우 괄호를 쓸 것
def sum2(c, d):
    print("%d, %d의 합은 %d입니다." % (c, d, c+d))

sum2(1, 2)
print(sum2(1,2)) #return값이 없기 때문에 None
#결과값이 없는 경우2
myList = [1,2,3]
print(myList.append(4)) # append함수는 return값이 없기 때문에 None이 출력
print(myList.pop()) # pop함수는 위에 append로 추가한 4라는 값이 출려된다. 즉 return값이 있는 함수

#3️⃣입력과 결과 다 없는 경우 / 입력값과 결과값이 없기에 함수를 출력하면 None이 출력
def say2():
    print("Hi")
print(say2()) # 우연히 찾은 결과 - 괄호 없이 함수명만 쓸 경우(print(say2)), 함수의 주소값이 출력된다

#4️⃣여러 개의 입력값
def sum_many(*args): 
    #입력값이 몇 개 인지 알 수 없을 경우, *args로 변수를 주면 모두 입력 받을 수 있다. / *뒤에 변수명은 자유이나 일반적으로 args를 많이 쓴다.
    #변수와 입력값이 다른 경우(ex) 변수: a,b,c,d,e / 입력값: 1,2), 변수와 입력값의 갯수가 달라 에러가 발생한다.
    sum = 0
    for i in args:
        sum = sum + i
    return sum
print(sum_many(1,2,3))

#5️⃣딕셔너리 형태로 출력되는 경우(키워드 파라미터(keyword arguments)) 
def print_kwargs(**kwargs):
    for k in kwargs.keys():
        if(k == "name"):
            print("당신의 이름은 :"+k)
print(print_kwargs(name = "int 조수", b="2"))

#6️⃣함수의 결과값은 하나
def sum_and_mul(a,b):
    return a+b, a*b, a-b
    #결과값이 tuple로 묶여서 나온다. / 값을 여러개 return 하지만 튜플로 묶여서 반환하기 때문에 tuple에서 원하는 값을 꺼내써야한다.
print(sum_and_mul(1,2))
print(sum_and_mul(1,3)[0]) #0번째 인덱스의 값만 tuple에서 꺼내서 출력한다.

#7️⃣매개변수에 초기값 미리 설정하기
def say_myself(name, old, man=True): 
    #man을 True라고 미리 설정하였기 때문에 입력이 없을 경우 기본적으로 True가 된다.(입력이 있으면 바뀜)
    #변수의 순서에 유의할 것. 입력값과 순서가 맞지 않는 경우, 오류가 발생한다.
    #고정하고자 하는 초기값의 경우, 가장 마지막에 작성해야 한다. 입력 시 문제가 발생하기 때문.
    print("나의 이름은 %s입니다." % name)
    print("나이는 %d입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")
say_myself("우왁굳", 35)
say_myself("아이네", 28, False)

#8️⃣함수 안에 선언된 변수의 효력 범위
#함수 안에서 선언된 변수는 함수 안에서만 효력을 발휘한다.(지역변수)
a = 1
def vartest(a):
    a = a + 1

vartest(a)
print(a)

#9️⃣함수 안에서 함수 밖의 변수를 변경하는 법1
b = 1
def vartest2(b):
    b = b + 1
    return b #return값 설정

b = vartest2(b) #함수의 return값(지역변수)을 전역변수에 할당한다.
print(b)

#함수 안에서 함수 밖의 변수를 변경하는 법2(global)
c = 1
def vartest3():
    global c # 전역변수로 선언
    c =  c + 1

vartest3()
print(c)

#🔟lamda
#일반적인 함수 정의 / list 등에서는 사용하기 힘들다.
# def add(a,b):
#     return a+b
#lamda함수로 정의할 경우
add = lambda a, b: a+b
print(add(1,2))
#list를 활용한 경우
realList = [lambda a, b: a+b, lambda a, b: a*b, lambda a, b: a-b]
print(realList[0](1,2)) # 0번째 인덱스의 lambda함수를 호출하여 변수를 입력한다.
