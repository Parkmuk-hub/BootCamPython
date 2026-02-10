print('__________________________________________________')

var1 = "안녕 파이썬"
print(var1), # 이건 주석
"""
var은 주소를 저장함
var을 출력하면 주소에 저장된 값을 출력함
변수 _로 시작해도 괜찮음
앵간하면 영어로 하자
"""
print('__________________________________________________')

var1 = 5; # 인퍼프리터 방식으로 타입 지정 안해도 자동 지정
var1 = 10;
var1 = 5.6;
print(var1)
var2 = var1
print(var1, var2)
var3 = 7
print(var1, var2, var3)
print(id(var1), id(var2), id(var3))
Var3 = 8
print(var3, Var3)

print('__________________________________________________')

a = 5
b = a
c = b
print(a, b, c)
print( a is b, a == b ) # 'is'는 주소 비교 연산,  " == " 은 값 비교 연산
print( b is c, b == c )

print('__________________________________________________')

aa = [5, 4, 3]
bb = [0, 1, 2]

print( aa[1], bb[0] )
print( aa[2], bb[1] )

print ( aa is bb, aa == bb )

print('__________________________________________________')

import keyword # 키워드 목록 확인용 모듈 읽기

print('예약어 목록:',  keyword.kwlist) 

print('__________________________________________________')

print('type(자료형) 확인')

kbs = 9
print(isinstance(kbs, int))
print(isinstance(kbs, float))
print(5, type(5)) # int
print(5.1, type(5.1)) # float
print(3 + 4j, type(3 + 4j)) # complex
print(True, type(True)) # bool
print('good', type('good')) # str
print((1,), type((1,))) # tuple
print([1], type([1])) # list
print({1}, type({1})) # set
print({'k':1}, type({'k':1})) # dict

print('__________________________________________________')
