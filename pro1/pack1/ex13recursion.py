# 재귀함수 : 함수가 자기 자신을 호출 - 반복처리

def countDown(n) :
    if n == 0 :
        print('완료')
        #return 1
        # return 넣어주면 좋음
    else :
        print(n, end = " ")
        #return n + countDown(n - 1) # <= 재귀 호출
        countDown(n - 1)
# dap = countDown(5)
# print(dap)
countDown(5)
# 5 4 3 2 1 완료

print("\n",'__________________________________________________',"\n")
print('1 ~ n 까지 합')
def totFunc(n):
    if n == 0 :
        print('탈출')
        return 1 # True 반환
    return n + totFunc(n - 1) # <== 재귀 호출
"""
1 ~ n 까지 합
탈출
result :  16
"""

result = totFunc(5)
print("result : ", result)

print("\n",'__________________________________________________',"\n")
print('5 factorial(계승)')

def factoFunc(a) :
    if a == 1 : return 1
    print(a, end = " ")
    return a * factoFunc(a - 1)

result2 = factoFunc(5)
print(result2)

print('end')
"""
5 factorial(계승)
5 4 3 2 120
end
"""


