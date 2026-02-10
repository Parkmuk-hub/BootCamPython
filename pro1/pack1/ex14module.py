# Module : 소스 코드의 재사용을 가능하게 하며, 소스 코드를 하나의 이름 공간으로 구분하고 관리함
# 하나의 file은 하나의 모듈이 된다. 
# 표준 모듈, 사용자 작성 모듈, 제 3자 모듈(third party)로 구분할 수 있다.  
print(print.__module__) # builtins

print('뭔가를 하다.... 외부 모듈 사용하기')
import sys
print(sys.path)

print("\n",'__________________________________________________',"\n")

a =  5
if a > 7 :
    sys.exit()

import math
print(math.pi) 

print("\n",'__________________________________________________',"\n")

import calendar
calendar.setfirstweekday(6)
calendar.prmonth(2026, 2)
del calendar

print("\n",'__________________________________________________',"\n")

import random # 모듈

print(random.random())
print(random.randrange(1, 10))

from random import random, choice, randrange # 모듈의 멤버를 계속 호출하기 귀찮을 때 사용
from random import *
print(random())


print('end')

# sys.exit() #  응용프로그램 강제 종료

