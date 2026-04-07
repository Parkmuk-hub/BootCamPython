# sigmoid function 적용 연습
# 로지스틱 회귀에서는 wx + b 자체는 logit한 값이다. 
# log(p - (1 - p)) = wx + b 라고 정의됨
# 그러므로 z = wx + b --> sigmoid(z) --> p(0 ~ 1)

# 시그모이드 함수 수식으로 반환된 값 확인
import math
def sigmoidFunc(num) :
    return 1 / (1 + math.exp(-num))

print(sigmoidFunc(3))   # 0.9525741268224334
print(sigmoidFunc(1))   # 0.7310585786300049
print(sigmoidFunc(-5))  # 0.0066928509242848554
print(sigmoidFunc(-10)) # 4.5397868702434395e-05
# 양수는 0.5보다 크고 음수는 0.5보다 많이작다

import numpy as np
import matplotlib.pyplot as plt
import koreanize_matplotlib

print("\n 로짓(logit)변환된(가정) 값으로 시그모이드 함수 통과 후 그 결과를 시각화")
x = np.linspace(-10, 10 ,50)    #  입력 자료(연속형)
print(x)

# 선형결합(이미 logit값)
w = 1.5
b = -2
z = w * x + b

def sigmoid(z) :
    return 1 / (1 + np.exp(-z))

p = sigmoid(z)     # 확률값 얻음
print('p :\n', p)

# 일부 값 보기
print("x[:3] : ", np.round(x[:3], 3))        # [-10.     -9.592      -9.184]
print("z[:3](logit) : ", np.round(z[:3], 3)) # [-17.    -16.388      -15.776]
print("p[:3](확률) :", p[:3])                # [4.13993755e-08 7.63639448e-08 1.40858451e-07]

# 시각화 
plt.figure(figsize=(8, 5))
plt.plot(x, p, label='sigmoid(z)', c="b")
plt.axhline(0.5, c="r", linestyle="--")
plt.title("z = wx + b --> sigmoid --> 확률")
plt.xlabel("x(입력값)")
plt.ylabel("y(확률값)")
plt.grid(True)
plt.legend()    # label과 짝궁
plt.show()



