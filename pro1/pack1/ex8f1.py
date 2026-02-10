#function : 여러 개의 수행문을 하나의 이름으로 묶은 실행 단위
# 함수 고유의 실행 공간을 갖음
# 자원의 재활용

# 내장함수 일부 체험

print(sum([1, 2, 3]))
print(bin(8))
print(eval('4 + 5'))
print(round(1.2), round(1.6)) # 5를 기준으로 반올림함

import math
import random
print(math.ceil(1.2), ' ', math.ceil(1.2)) # 소수점 있으면 하나 올림
print(math.floor(1.2), ' ', math.floor(1.2)) # 소수점 무시함

b_list = [True, 1, False]
print(all(b_list)) # 모두 참이면 참
print(any(b_list)) # 하나라도 참이면 참

data1 = [10, 20 ,30]
data2 = ['a', 'b', 'c']
for i in zip(data1, data2) :
    print(i)