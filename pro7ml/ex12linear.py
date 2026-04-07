# Linear Regression 클래스 사용 : 평가 score 정리
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression   # summary() 지원 안함
from sklearn.metrics import r2_score, explained_variance_score, mean_squared_error
from sklearn.preprocessing import MinMaxScaler      # 정규화 클래스

# 데이터 생성
sample_size = 100
np.random.seed(1)

x = np.random.normal(0,10,sample_size)
y = np.random.normal(0,10,sample_size) + x*30
print(x[:5])
print(y[:5])
print('상관 계수 : ', np.corrcoef(x,y)[0,1])

# 독립변수 x를 정규화하기(0~1 사이의 범위 내에 자료로 변환)
scaler = MinMaxScaler()             # 객체 하나 생성
x_scaled = scaler.fit_transform(x.reshape(-1,1))            # 1차원을 2차원으로 바꿈 sklearn은 2차원 배열을 필요로 하기 때문이다.
print(x[:5])
print(x_scaled[:5])

# 시각화
plt.scatter(x, y)
plt.scatter(x_scaled, y)
plt.show()

model = LinearRegression().fit(x_scaled,y)
print('model : ', model)
print('회귀계수(slope) : ', model.coef_)
print('회귀계수(intercept, bias) : ', model.intercept_)
print('결정계수(R^2) : ', model.score(x_scaled, y))
y_pred = model.predict(x_scaled)        # 예측된 y
print('예측값 : ', y_pred[:5])
print('실제값 : ', y[:5])

# 모델 성능 확인 함수 작성
def myRegScoreFunc(y_true, y_pred):
    # 결정계수 : 실제 관측값의 분산대비 예측값의 분산을 계산하여 데이터 예측의 정확도 성능 측정
    print(f'r2_score(결정계수) : {r2_score(y_true, y_pred)}')
    # 모델이 데이터의 분산을 얼마나 잘 설명하는지 나타내는 지표(오차 분산이 작으면 점수 높음)
    print(f'explained_variance_score(설명분산점수) : {explained_variance_score(y_true, y_pred)}')
    # 오차를 제곱해 평균 구함( 오차가 커질수록 손실함수 값이 빠르게 증가함. 값이 작으면 모델 성능 우수
    print(f'mean_squared_error(MSE, 평균제곱오차) : {mean_squared_error(y_true, y_pred)}')
    imsi = mean_squared_error(y_true, y_pred)          #RMSE로 변환해서 확인
    print(f'mean_squared_error(RMSE, 평균제곱오차) : {np.sqrt(imsi)}')   # 9.28159

myRegScoreFunc(y, y_pred)       # 실제 값, 예측 값

print('분산이 크게 다른 x,y 값을 사용 --------')
x2 = np.random.normal(0,1,sample_size)
y2 = np.random.normal(0,100,sample_size) + x * 30
print(x2[:5])
print(y2[:5])
print('상관 계수 : ', np.corrcoef(x2,y2)[0,1])              # -0.054844


x_scaled2 = scaler.fit_transform(x2.reshape(-1,1))
model2 = LinearRegression().fit(x_scaled2,y2)
print('model : ', model2)
print('회귀계수(slope) : ', model2.coef_)
print('회귀계수(intercept, bias) : ', model2.intercept_)
print('결정계수(R^2) : ', model2.score(x_scaled2, y2))          # 0.003007
# 분산이 너무 큰 모델을 그대로 사용하는 것은 의미가 없다.