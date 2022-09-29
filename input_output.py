#사용자 입력과 출력

#1️⃣input
a = input()
print(a)
#input함수로 인자를 넣을 수 있다.
number = input("숫자를 입력하시오: ")
print(number)

#2️⃣print
print("life" "is" "too short") #lifeistoo short
print("life", "is", "too short") #life is too short / 띄어쓰기가 된다.
for i in range(10):
    print(i, end = ' ') #줄바꿈 없이 한 줄로 출력