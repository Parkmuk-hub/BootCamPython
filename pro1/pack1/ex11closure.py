# Closure : Scope에 제약을 받지 않는 변수들을 포함하고 있는 코드블럭이다.
# 내부 함수의 주소를 반환해 함수 밖에서 함수 내의 멤버를 참조한다.

def funcTimes(a, b):
    c = a * b
    return c

print(funcTimes(2, 3))

kbs = funcTimes(2, 3)
print(kbs)
kbs = funcTimes
print(kbs)
print(kbs(2, 3))
print(id(kbs), id(funcTimes))
tvn = sbs = kbs

del funcTimes
# print(funcTimes(2, 3))
print(tvn(2, 3))

print("\n",'__________________________________________________',"\n")
print("클로저를 사용하지 않은 경우")
def out() :
    count = 0
    count += 1
    return count

    


print(out())
print(out())

print("\n",'__________________________________________________',"\n")
print("클로저를 사용하는 경우")
def outer() :
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner # <== 이게 클로저 : 내부함수의 주소를 반환

var1 = outer() # 내부함수의 주소를 변수에 저장[함수에 ()없으면 주소를 줌]
print('var1 주소 :', var1)
print(var1())
print(var1())
myvar = var1()
print(myvar)
print()
var2 = outer() # 새로운 객체(inner 함수) 생성
print(var2())
print(var2())

print(var1, "\n",var2)

print("수량 * 단가 * 세금 한 결과를 출력하는 함수")
def outer2(tax) : # tax는 지역 변수 (함수 안에서 놀고 있는 파라미터 모두 지역 변수)
    def inner2(su, dan) :
        amount = su * dan * tax
        return amount
    return inner2 # inner2가 closure입니다. 

# 1분기에는 su * dan 에 대한 tax는 0.1 부과

q1 = outer2(0.1) # inner2의 주소를 기억한다
result1 = q1(2, 10000)
print("1분기의 세금 : ", result1)
result2 = q1(5, 50000)
print("1.5분기의 세금 : ", result2)

# 2분기에는 su * dan 에 대한 tax는 0.05 부과
q2 = outer2(0.05)
result3 = q2(5, 50000)
print("2분기의 세금 : ", result3)
result4 = q2(2, 10000)
print("2분기의 세금 : ", result4)

print('\n 일급함수 : 함수안의 함수, 인자로 함수 전달, 반환 값이 함수')

def func1(a, b) :
    return a + b

func2 = func1
print(func1(3, 3))
print(func2(3, 3))
print()
def func3(fu) : # 인자로 함수 전달
    def func4(): # 함수 안의 함수 선언
        print('나는 내부함수임')
    func4()
    return fu # 반환 값이 함수

tvn = func3(func1) # func1 = fu
print(tvn(3, 4))

print('\n 축약함수 (Lambda function) : 이름이 없는 한 줄짜리 함수')
# 형식 : lambda 매개변수들,,,: 반환식 <= return 없이 결과 반환
def hapFunc(x, y):
    return x + y
print(hapFunc(1, 2))
#lambda 표현
print((lambda x, y : x + y)(1, 2))

gg = lambda x, y: x + y
print(gg(1, 2))

kbs = lambda a, su = 10 : a + su
print(kbs(5))
print(kbs(5, 6))

sbs = lambda a, *tu, **di:print(a, tu, di) # *하나면 () 안에 출력, ** 두개면 {} 안에 출력
sbs(1, 2, 3, var1 = 4, var2 = 5)

li = [lambda a, b : a + b, lambda a, b : a * b]
print(li[0](3, 4))
print(li[1](3, 4))

print('\n다른 함수에서 람다 사용하기')
# filter(함수, 반복 가능한 객체)
print(list(filter(lambda a : a < 5, range(10))))
print(list(filter(lambda a : a % 2, range(10)))) # 짝수는 나머지 0이라 False, 홀수는 나머지 1이라 True

# 문1) filter 이용해서 1 ~ 100 사이의 정수 중 5의 배수이거나 7의 배수만 출력

print(list(filter(lambda a : a % 5 == 0 or a % 7 == 0, range(1, 101))))
