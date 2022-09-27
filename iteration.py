#반복문
# debugging으로 어떻게 실행되는지 참고해보자

# 1️⃣while문
treeHit = 0
while treeHit < 10:
    treeHit = treeHit + 1 # java처럼 증감연산자(i++ / i-- / ++i / --i)가 없다  
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무가 넘어갑니다.")    
# break - while문을 종료한다
coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee -1
    print("남은 커피의 양은 %d 입니다." % coffee)
    if not coffee: # 정수가 있는 경우, True로 인식하기에, not True = False / coffee가 0이 되는 순간 False가 되기에, not False = True가 된다.
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break
# continue - while문의 맨 처음으로 돌아간다.
a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0:
        continue 
    print(a)
# 무한루프 - ctrl+c로 끊을 수 있다.
# while True:
#     print("test")

# 2️⃣for문
test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)
#list, tuple 등의 혼합형태
a = [(1,2), (3,4), (5,6)] #list 안에 tuple
for (first, last) in a: #tuple 값을 받게 작성
    print(first + last)
#예문1
marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number = number + 1
    if mark >= 60:
        print("%d 학생은 합격" % number)
    else:
        print("%d 학생은 불합격" % number)
#예문2
number_two = 0
for mark2 in marks:
    number_two = number_two + 1
    if mark2 < 60:
        continue
    print("%d번 학생 합격입니다." % number_two)
#range 함수 - 다른 언어에서의 for문 형식?
sum = 0
for i in range(1, 11): # 1이상 11 미만 == 1~10
    sum = sum + i
print(sum)
#이중 for문(구구단)
for i in range(2, 10):
    for j in range(1, 10):
        print(i*j, end =" ") 
        #end는 print의 옵션 중 하나 / end를 사용할 경우 줄바꿈을 하지 않고 이어서 출력 / 공백을 넣은 경우 띄어쓰기로 사용가능
    print('') #줄바꿈용
#list 내포(List comprehension)
result = [x*y for x in range(2, 10) for y in range(1, 10)]
print(result)
#위의 내포형식을 풀어쓸 경우 아래와 같다.
result = []
for x in range(2, 10):
    for y in range(1, 10):
        result.append(x*y)