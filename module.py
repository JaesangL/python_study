#모듈(module)
#미리 만들어놓은 .py파일(함수, 변수, 클래스)
import mod #mod에 작성한 것을 가져와서 사용
print(mod.add(1,2))

#하나의 기능만 가져오고 싶은 경우
#from 파일명 import 원하는 기능명

#import하려는 파일 중에 실행시키고 싶지 않은 경우 해당 파일에 조건을 걸어놓아야 한다.

#가져오고 싶은 파일의 경로가 다를 경우 경로 설정을 해주어야한다.
#sys.path.append
import sys
sys.path.append("D:\PythonCoding\sys_path_append")
import mod2
print(mod2.div(6,2))