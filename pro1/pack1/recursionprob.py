"""
재귀문제 :  리스트 자료 v = [7, 9, 15, 43, 32, 21] 에서 최대값 구하기 - 재귀 호출 사용 

print(find_max(v, len(v)))
"""

def max(x, y) :
    if x > y :
        return x
    else :
        return y

def find_max(array, len) :
    if len == 1 :
        return array[0] 
    else :
        return max(array[len - 1], find_max(array, len - 1))
    
v = [7, 9, 15, 43, 32, 21]

print("최대값 : ",find_max(v, len(v)))

def min(x, y) :
    if x < y :
        return x
    else :
        return y
    
def find_min(array, len) :
    if len == 1 :
        return array[0]
    else :
        return min(array[len - 1], find_min(array, len - 1))
    
v = [7, 9, 15, 43, 32, 21]

print("최소값 : ",find_min(v, len(v)))

"""
"리스트 값은 배열과 똑같다"
파이썬의 리스트는 다른 언어의 배열(Array)과 같은 역할을 하죠. 
데이터들을 줄 세워 놓고 인덱스([0], [1])로 접근한다는 개념을 정확히 잡으셨네요.

"이런 계산 문제는 array와 len을 이용하여 풀자"
데이터(array)와 그 데이터의 크기(len)는 실과 바늘 같은 존재예요. 
특히 재귀나 반복문을 쓸 때 "어디까지 계산할 것인가"를 결정하는 기준이 바로 len이기 때문입니다.

"최대값을 어떻게 구할지 def로 정의하여 출력정의문에서 사용하자"
이게 바로 프로그래밍의 핵심인 **'함수화(Modularization)'**입니다. 
max나 min처럼 작은 논리를 따로 분리해두면, 
나중에 find_max든 find_min이든 어디서든 재사용할 수 있어 코드가 훨씬 읽기 편해집니다.

"""
def find_ax(v, n):
    if n == 1 :
        return v[0]
    prev_max = find_ax(v, n-1)

    if v[n - 1] > prev_max :
        return v[n-1]
    else :
        prev_max

v = [7, 9, 15, 43, 32, 21]

print("최대값 : ",find_ax(v, len(v)))
