#조건문(if문)
from email import message


money = False
if money:
    print("택시를 타고 가라")
else: 
    print("걸어 가라")

# 들여쓰기 주의할 것
money = True
if money:
    print("택시를 타고 가라")
#print("aa") - SyntaxError: invalid syntax
else: 
    print("걸어 가라")
# 1️⃣비교연산자(< / > / == / != / <= / >=)
a = 1
b = 2
if a > b:
    print("택시타기")
else:
    print("걸어가기")
#예문
fee = 2000
if fee >= 3000:
    print("택시")
else:
    print("걷기")
# 2️⃣and (둘 다 True일 경우에 전체가 True, 기호: & ) /  or(둘 중 하나라도 True이면 전체가 True, 기호: | )  
# not(True, False를 바꾼다, not True == Fasle / not False == True)
taxiFee = 2000
card = 1
if taxiFee >= 3000 or card: 
    # or 기호( | ) 사용 시 앞의 조건을 괄호()로 감싸주지 않는 경우 뒤의 숫자를 int로 인식하는 듯 하다. ex)if (taxiFee >= 3000) | card:
    # 괄호를 사용하지 않을 경우, or 사용 시에는 정상 결과가 출력되나 기호를 사용하면 else의 결과를 출력함
    # and의 경우도 동일
    print("택시가능")
else:
    print("뚜벅뚜벅")

# 3️⃣in / not in
# if (찾고자 하는 값) in (list, tuple 등의 자료형) / 찾고자 하는 값이 있을 경우 True를 return한다. / not in은 반대
m = 2000
credit = 1
if 1 in [1, 2, 3]:
    print("taxi")
else:
    print("walk")

# 4️⃣pass(조건문에서 아무 일도 하지 않게 설정하고 싶다면 / 결과를 따로 출력하고 싶지 않은 경우)
m1 = 2000
credit1 = 1
if 1 in [1, 2, 3]:
    pass
else:
    print("walk")

# 5️⃣elif(java의 else if)
pocket = ["paper", "cellphone"]
card = False
a = True
if "money" in pocket:
    pass
elif card:
    print("take a taxi")
elif a:
    print("aa")
else:
    print("just walk")

# 6️⃣조건부 표현식(파이썬의 간결한 표현? / 다른 언어의 3항 연산자(기호: ?)의 파이썬식 방법)
#일반적인 작성법
score = 70
if score >= 60:
    message = "success"
else:
    message = "failure"
print(message)
#표현식
message = "success" if score >= 80 else "failure" # 조건부 표현식의 경우 else가 없으면 오류 발생
print(message)

#3항 연산자 예제
"""int main()
{
	int a = 200;
	int b = 100;
		
	a > b ? printf("a가 크네") : printf("b가 크네");
}"""