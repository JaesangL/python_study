#파일 읽고 쓰기
#1️⃣파일 생성
# f = open("새파일.txt", "w") #새파일.txt를 생성하고 w(쓰기모드) 설정 / r: 읽기 a: 추가(파일 마지막에 새로운 내용 추가)
# f.close()

#2️⃣쓰기
f = open("D:\PythonCoding\\test\새파일2.txt", "w", encoding="UTF-8") 
#경로 설정 가능 D:\PythonCoding\test/새파일2.txt(절대경로), \test/새파일2.txt(상대경로)
#\를 \\로 해야 유니코드 에러가 안난다. / 에러 발생 시 - OSError: [Errno 22] Invalid argument: 'D:\\PythonCoding\test\\새파일2.txt'
#인코팅 에러 발생 시 encoding 설정 해줄 것
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

#3️⃣읽기
# readline() 함수
f = open("test\새파일2.txt", "r", encoding="UTF-8") 
#폴더가 다른 경우 경로 설정이 필요하다. 위의 경우 상대경로로 설정
#인코딩을 안할 경우, 파일이 깨져서 읽을 수 없다.
line = f.readline() #한줄씩 읽는다.
print(line)
f.close()#파일을 열었을 경우, 무조건 닫아주어야한다.

#여러 줄을 읽으려는 경우
f = open("test\새파일2.txt", "r", encoding="UTF-8")
while True:
    line = f.readline()
    if not line: break #line이 False 일 경우 = 공백일 경우, not을 붙여 True로 변환
    print(line)
f.close()
#readline"s"
f = open("test\새파일2.txt", "r", encoding="UTF-8")
lines = f.readlines()
for line in lines:
    #print(line)#작성 시 \n이 썼기 때문에 print함수의 자체 줄바꿈 + \n으로 한줄씩 띄어져서 출력된다.
    #print(line, end="")
    print(line.strip("\n")) #양쪽 끝에서 특정 문자를 제거해주는 함수(2강 문자열 참고)
f.close()

#read() 함수 
f = open("test\새파일2.txt", "r", encoding="UTF-8")
data = f.read() # 파일을 통째로 읽는 것
print(data)
f.close()

#3️⃣추가 add
#write과 차이점 - write(w)은 기존의 내용을 지우고 새롭게 작성 / add(a)는 기존의 내용에 추가로 작성
f = open("test\새파일2.txt", "a", encoding="UTF-8")
for i in range(11,20):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close

#4️⃣with문과 함께 사용하기 / close함수 사용안하는 방법
with open("foo.txt", "w") as f: #f는 지역변수 이기에 with문을 빠져나가면 자동으로 close된다.
    f.write("Life is too short, you need Python")
