print("Hello, World")
a = 4
b = 3
print("더하기: "+str(a+b)) #더하기
print("곱하기: "+str(a*b)) #곱하기
print("나누기: "+str(a/b)) #나누기
print("몫: :"+str(a//b)) #몫
print("나머지: "+str(a%b)) #나머지

#1️⃣Indexing
c = "Life is too short, you need Python"
print("First index is "+str(c[0]))

#2️⃣Slicing
print(c[0:4]) #[ (이상) : (미만) : (간격) ]

d = "20010331Rainy"
print(d[:8])
print(d[8:])

f = "123456789"
print(f[::1])
print(f[::2])

#3️⃣Str formatting
g = "I eat %d apples." % 3
print(g)

number = 10
day = "three"
h = "I ate %d apples. so I was sick for %s days" % (number, day)
print(h)

i = "test test {} formatting test".format("안녕")
j = "test {age} test {name} formatting test".format(name="아이네", age=28)
print(i)
print(j)

name = "int"
k = f"나의 이름은 {name}입니다."
print(k)

#4️⃣decimal point(소수점 자르기)
l = "%0.4f" % 3.42134234
print(l)

#5️⃣count
m = "hobby"
count = m.count('b') #해당 str에 'b'가 총 2개
print(count)

#6️⃣find(인덱스를 세는 것)
find = m.find('b')
print(find) # 2가 나온 이유는 0=h, o=1, b=2이기 때문
print(m.find('x')) # 찾는 것이 없을 경우 -1을 리턴

#7️⃣join(기준으로 쪼개기)
n = ",".join("abcd") #","를 기준으로 문자 쪼개기
print(n)

nArray = ",".join(["a", "b", "c"]) #list를 str로 리턴
print(nArray)

#8️⃣대소문자, 공백 지우기
upper = "hi"
lower = "HI"
strip = "   HI   "
print(upper.upper())
print(lower.lower())
print(strip.strip())

#9️⃣replace
o = "Life is too short"
print(o.replace("Life", "Your leg"))

#🔟split
print(o.split())
sTest = "a:b:c:d"
print(sTest.split(':'))

#🔟1️⃣list(indexing, slicing 등 적용 가능)
isd = ["아이네", "징버거", "릴파", "주르르", "고세구", "비챤"]
print(isd[1])
print(isd[0:3])
wakta = [1, 2, "우왁굳",["아이네", "징버거", "릴파", "주르르", "고세구", "비챤"]]
print(wakta[3])
print(wakta[3][0])

print(isd + wakta) #list 줄바꿈은 str로 변환 후밖에 안되나..?
wakta[0] = "뢴트게늄"
print(wakta)
wakta[1:2] = ["히키킹", "풍신"]
print(wakta)
wakta[0:3] = []
print(wakta)
wakta[0] = ["test", "test1"]
print(wakta)
del wakta[1] # 삭제
print(wakta)

#🔟2️⃣append
isd.append("뢴트게늄")
print(isd)

#🔟3️⃣sort(정렬) sort 함수는 list 정렬 '기능'일 뿐 리턴값이 없다(None) 리턴값이 필요한 경우 sorted 함수 이용하기!
isd.sort() # function의 () 잊지 말고 쓰기!!
print(isd)

#🔟4️⃣reverse
isd.reverse()
print(isd)

#🔟5️⃣index
print(isd.index("아이네"))

#🔟6️⃣insert(특정 index에 추가)
isd.insert(0, "우왁굳")
print(isd)

#🔟7️⃣remove(특정 값을 제거) del은 인덱스를 찾아 삭제, remove는 값을 삭제
isd.remove("우왁굳")
print(isd)

num = [1, 2, 3, 5, 1, 1, 1, 1]
num.remove(1) #가장 먼저 찾은 값만 삭제
print(num) 

#for문 테스트
for num2 in num[::]:
    if num2 == 1:
        num.remove(num2)
print(num)

#🔟8️⃣pop(list의 마지막 값을 꺼내서 list에서 제외 / 꺼낸 값은 사라진다)
print(isd.pop())
print(isd)

#🔟9️⃣count(list에 포함된 요소 세기)
print(num.count(1)) #for문으로 1을 모두 삭제하여 없다
print(num.count(5))

#🔟🔟extend(list 추가)
isd.extend(["우왁굳, 고멤"]) #list가 추가되는 것이 아닌 list의 값이 추가되는 것
print(isd)
