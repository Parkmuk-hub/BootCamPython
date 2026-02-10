# 사용자 정의 함수
"""

def 함수명(가인수,,,):
    return 반환값 # 1개만 반환, return이 없으면 return None

함수명(실인수,,,): # 함수 호출
    
"""

def doFunc1() :
    print('doFunc1 수행')
def doFunc2(name) :
    print('name : ', name)
def doFunc3(arg1, arg2) :
    re = arg1 + arg2
    return re

def doFunc4(a1, a2) :
    imsi = a1 + a2
    if imsi % 2 == 1 :
        return
    else :
        return imsi

doFunc1() # 함수 호출
print('함수 주소는 ', doFunc1)
print(' 함수 주소는 ', id(doFunc1))
print(doFunc1) # 객체 주소를 가지고있음

imsi = doFunc1
imsi()
print(doFunc1())

print("\n",'__________________________________________________',"\n")

doFunc2(7)
doFunc2("길동")
# doFunc2("길동", "순신")
print("\n",'__________________________________________________',"\n")

doFunc3("대한", "민국")
print(doFunc3("대한","민국"))
print(doFunc3(5, 6))
result = doFunc3("5", "6")
print(result)

print("\n",'__________________________________________________',"\n")

print(doFunc4(3, 4))
print(doFunc4(3, 5))

print("\n",'__________________________________________________',"\n")

def triArea(a, b) :
    c = a * b / 2
    triAreaPrint(c) # 다른 함수 호출

def triAreaPrint(cc) :
    print('삼각형의 면적은 :', cc)

triArea(20, 30)

print("\n",'__________________________________________________',"\n")

def passResult(kor, eng):
    ss = kor + eng
    ans = int(ss)
    if ans >= 50 :
        return True
    else :
        return False

if passResult(20, 50):
    print('합격')
else:
    print('불합격')

print("\n",'__________________________________________________',"\n")

def swapFunc(a, b):
    return b, a

a = 10 ; b = 20
print(a, ' ', b)
print(swapFunc(a, b))

print("\n",'__________________________________________________',"\n")

def funcTest():
    print('funcTest 멤버 처리')
    def funcInner() :
        print('내부 함수입니다.')
    funcInner()

funcTest()

print("\n",'__________________________________________________',"\n")
# if 조건식 안에 함수 사용
def isOdd(para) :
    return para % 2 == 1 # 홀수이면 True 반환

mydict = { x : x * x for x in range(11) if isOdd(x)}
print(mydict)

print("\n",'__________________________________________________',"\n")

print('변수의 생존 범위 (scope rule)')
# 변수가 저장되는 이름공간은 변수가 어디서 선언 되었는가에 따라 생존 시간이 다름
#전역, 지역 변수

player = '전국대표' # 전역변수 (현재 모듈 어디서든 호출 가능)
name = '차범근'

def funcSoccer() :
    name = '손흥민' # 지역변수 ( 현재 함수 내에서만 호출 가능)
    #player = '지역대표'
    city = "LA"
    print(f'이름은 {name} 수준은 {player}')
    print(f'지역은 {city}')

funcSoccer()
print(f'이름: {name} 수준: {player}')
# print(f'지역 : {city}')

print()
a = 10; b = 20; c = 30
def Foo() :
    a = 7
    b = 100 
    def Bar() :
        global c # Bar 함수의 멤버가 아니라 모듈의 멤버가 됨, 전역변수
        nonlocal b
        b = 8
        print(f'Bar 수행 후 a : {a}, b : {b}, c : {c}')
        b = 200 
        c = 9
    Bar()
    print(f'Foo 수행 후 a : {a}, b : {b}, c : {c}')

Foo()
print(f'함수 수행 후 a : {a}, b : {b}, c : {c}')
print("\n",'__________________________________________________',"\n")

g = 1
print(g)
def func() :
    global g
    a = g
    g = 2

    return a

print(func())

print(g)

"""
result = imsi
result2 = imsi()
print('result : ', result)
"""