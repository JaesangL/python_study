# Q1
lang = 80
eng = 75
math = 55
total = lang + eng + math
average = total/3
print("평균: "+str(average))
# Q1-1
testScore = [80, 75, 55]
result = 0
for val in testScore:
    result += val # 하나하나 더하기
print(f"average: {result / len(testScore)}")
# Q1-2
result2 = sum(testScore)
print(f"평균은: {result2 / len(testScore)}")
# Q1-3
import numpy as np

avg4 = np.mean(testScore)
print(f"avg is: {avg4}")
# Q1-4
import statistics

avg5 = statistics.mean(testScore)
print(f"평균이 {avg5}라니")


# Q2
num = 13
if num % 2 == 0:
    print("짝")
else:
    print("홀")

# Q2-1 함수 만들기
def check(num2):
    if num2 % 2 ==0:
        print("even")
    else:
        print("odd")
check(13)

# Q3
hong = "881120-1068234"
birth = hong.split("-")
print(birth)

# Q3-1
yymmdd = hong[:6]
serial = hong[7:]
print(yymmdd)
print(serial)

# Q4
pin = "881120-1068234"
gender = int(pin[7]) # 문자열->정수로 변환
print(gender)

# Q4-1
if gender == 1:
    print("man")
else:
    print("woman")

# Q5
a = "a:b:c:d"
print(a.replace(":", "#"))

# Q6
serialnum = [1, 3, 5, 4, 2]
serialnum.sort() # 리턴값이 없다. None. 리스트의 원형을 바꾼다.
print(serialnum)
serialnum.reverse() # 리턴값이 없다. None. 리스트의 원형을 바꾼다. 오직 list에서만 사용 가능
print(serialnum)

# Q6-1
sorting = sorted(serialnum) # 객체의 원형을 유지한다.
print(sorting) 
revering = list(reversed(sorting)) # iterator 로 꺼낸 값을 list로 다시 변경 / 객체의 원형을 유지한다. 리스트, 튜플, 스트링, 딕셔너리에서 사용 가능
print(revering)
# iterator 공부하기

# Q7
combine = ["Life", "is", "too", "short"]
combineStr = " ".join(combine) # 문자 띄어쓰기를 위해 공백 추가 / 문자열 이외의 타입이 있을 경우 에러가 발생할 수 있다.
print(combineStr)

# Q7-1 다른 타입이 섞인 경우
combineType = ["Life", "is", "too", "short", 10]
joined_str = ""
for v in combineType:
    if(len(joined_str) > 0):
        joined_str += " "
    joined_str += str(v)
print(joined_str)

# for문 연습
# 시험 점수가 60점 이상인 경우 합격이 출력되게 해라

score_list = [90, 45, 70, 60, 55]
number = 1

# Answer 1
for i in score_list:
    if i >= 60:
        print(f"{number}번 학생은 합격입니다.") # "{}번 학생은 합격입니다.".format(number)
    else:
        print(f"{number}번 학생은 불합격입니다.")
    number+=1

# Answer 2
score_list2 = [90, 45, 70, 60, 55]
number2 = 1
for i in score_list2:
    if i >= 60:
        final_score = "합격"
    else:
        final_score = "불합격"
    print(f"{number2}번 학생은 {final_score}입니다.") # "{}번 학생은 합격입니다.".format(number, final_score)
    number2+=1
