# 비선형회귀분석(Non-linear regression)
# : 직선의 회귀선을 곡선으로 변환해 보다 더 정확하게 데이터 변화를
#   예측하는데 목적이 있다.
# 선형가정이 어긋날 때 (비정규성) 대처할 수 있는 방법으로 
# 다항식 항을 추가한 다항회귀모델을 사용함
# 입력 데이터 특징 변환으로 선형모델을 개선

import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

x = np.array([1, 2, 3, 4, 5])
y = np.array([4, 2, 1, 3, 7])

plt.scatter(x, y)
plt.show()
print(np.corrcoef(x, y)[0, 1])  # 상관계수 : 0.48076197382041164 [비선형]

# 선형회귀모델을 적용
from sklearn.linear_model import LinearRegression # sklearn은 데이터를 2차원으로 달라함.
x = x[:, np.newaxis]    # 차원 확대. 1차원 -> 2차원으로
print(x)
# [[1]
#  [2]
#  [3]
#  [4]
#  [5]]
model = LinearRegression().fit(x, y)
y_pred = model.predict(x)
print('예측값 y : ', y_pred)    # [2.  2.7 3.4 4.1 4.8]
print('결정계수 : ', r2_score(y, y_pred))   #  0.23113207547169834

plt.scatter(x, y)
plt.plot(x, y_pred, c="r")
plt.show()      # 좋은 모델은 아님

# 비선형 모델 작성
# 여러 방법 중 가장 일반적인 방법을 사용(PolynomialFeatures, log변환, curve_fit)
from sklearn.preprocessing import PolynomialFeatures    # <== 다항식 특징을 추가
poly = PolynomialFeatures(degree=2, include_bias=False) # degree = 열 개수
x2 = poly.fit_transform(x)  # 특징 행렬을 만듦
print('\n', x)  # 5행 1열   5 by 1
print(x2)       # 5행 2열
# [[ 1.  1.]
#  [ 2.  4.]
# ...
model2 = LinearRegression().fit(x2, y)  # 특징 행렬값으로 모델 생성
ypred2 = model2.predict(x2)
print('예측값 y : ', ypred2)   # [4.14285714 1.62857143 1.25714286 3.02857143 6.94285714]

plt.scatter(x, y)
plt.plot(x,  ypred2, c="r") 
plt.show()  # degree = 2 일때 괜찮은 결과, degree = 5 일때 과적합


