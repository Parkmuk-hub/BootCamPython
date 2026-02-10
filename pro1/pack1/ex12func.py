# 함수 장식자 
# 기존 함수 코드를 고치지 않고 함수의 앞/뒤 동작을 추가할 수 있음
# 함수를 받아서 기능을 덧붙인 새 함수로 바꿔치기 가능
# meta 기능이 있음

def make2(fn) :
    return lambda : "안녕 " + fn()

def make1(fn) :
    return lambda : "디지몬 " + fn()

def hello() :
    return "아구몬"

hi = make2(make1(hello))
print(hi()) # 그냥 hi하면 주소, 뒤에 () 붙이면 값을 출력함

print()

@make2
@make1
def hello2() :
    return "파닥몬"

print(hello2())

print("\n",'__________________________________________________',"\n")
def traceFunc(func) :
    def wrapperFunc(a, b) :
        r = func(a, b)
        print(f'함수명 : {func.__name__}(a = {a}, b = {b} -> {r})')
        return r # 함수 반환 값을 반환
    
    return wrapperFunc # 함수 주소 반환 closure

@traceFunc #장식자
def addFunc(a, b) :
    return a + b

print(addFunc(10, 20))

