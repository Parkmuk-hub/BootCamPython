# # 회귀분석 문제 1) scipy.stats.linregress() <= 꼭 하기 : 심심하면 해보기 => statsmodels ols(), LinearRegression 사용
# 나이에 따라서 지상파와 종편 프로를 좋아하는 사람들의 하루 평균 시청 시간과 운동량에 대한 데이터는 아래와 같다.
# - 지상파 시청 시간을 입력하면 어느 정도의 운동 시간을 갖게 되는지 회귀분석 모델을 작성한 후에 예측하시오.
# - 지상파 시청 시간을 입력하면 어느 정도의 종편 시청 시간을 갖게 되는지 회귀분석 모델을 작성한 후에 예측하시오.
# 참고로 결측치는 해당 칼럼의 평균 값을 사용하기로 한다. 이상치가 있는 행은 제거. 운동 10시간 초과는 이상치로 한다.  

from scipy import stats
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import koreanize_matplotlib

# 1. 데이터 불러오기
data = pd.read_csv("지상파.csv")

# 2. 전처리 (조건대로 청소하기)
# [이상치] 운동 10시간 초과 데이터 제거 (35시간 데이터 삭제)
data = data[data['운동'] <= 10]

# [결측치] 지상파 칼럼의 NaN을 지상파 평균값으로 채우기
data['지상파'] = data['지상파'].fillna(data['지상파'].mean())

# 분석하기 편하게 변수에 담기
exer = data.운동
tvrun = data.지상파
tvend = data.종편


# 3. 모델 만들기 및 예측 (지상파 -> 운동 시간)

# 모델 생성 및 학습
model_exercise = smf.ols('운동 ~ 지상파', data=data).fit()

# 예측용 데이터 만들기 (지상파 3시간 시청 시)
new_data = pd.DataFrame({'지상파': [3.0]})
pred_exercise = model_exercise.predict(new_data)

print(f"지상파 3시간 시청 시 예상 운동 시간: {pred_exercise[0]:.2f}시간")

# 4. 검증하기 (scipy.stats.linregress 사용)

# 원본 데이터를 넣어서 기울기와 절편 뽑기
model1 = stats.linregress(tvrun, exer)

print('--- mo1 분석 결과 ---')
print('mo1 기울기(slope) : ', model1.slope)
print('mo1 절편(intercept) : ', model1.intercept)
print('mo1 p-value : ', model1.pvalue) 
print('-----------------')


# 5. 시각화 (그림 그리기)

# 실제 데이터 점 찍기
plt.scatter(tvrun, exer, label='실제 데이터')

# 회귀선 그리기 (y = ax + b)
plt.plot(tvrun, model1.slope * tvrun + model1.intercept, c='r', label='회귀선')

# 내가 예측한 '3시간' 지점 별표 찍기
plt.scatter([3.0], [pred_exercise[0]], c='blue', s=150, marker='*', label='3시간 예측값')

plt.xlabel('지상파 시청시간')
plt.ylabel('운동 시간')
plt.legend()
plt.show()


# 1. 모델 만들기 및 예측 (지상파 -> 종편)

# 모델 생성 및 학습
model_tvEnd = smf.ols(formula="종편 ~ 지상파", data=data).fit()
# 예측용 데이터 만들기 (지상파 3시간 시청 시)
pred_tvEnd = model_tvEnd.predict(new_data)
print(f"지상파 3시간 시청시 예상 종편 시청 시간 : {pred_tvEnd[0]:.2f}시간")

# 4. 검증하기 (scipy.stats.linregress 사용)

# 원본 데이터를 넣어서 기울기와 절편 뽑기
model2 = stats.linregress(tvrun, tvend)
print('--- mo2 분석 결과 ---')
print('mo2 기울기(slope) : ', model2.slope)
print('mo2 절편(intercept) : ', model2.intercept)
print('mo2 p-value : ', model2.pvalue) 
print('-----------------')


# 5. 시각화 (그림 그리기)

# 실제 데이터 점 찍기
plt.scatter(tvrun, tvend, label='실제 데이터')

# 회귀선 그리기 (y = ax + b)
plt.plot(tvrun, model2.slope  * tvrun + model2.intercept, c='r', label='회귀선')

# 내가 예측한 '3시간' 지점 별표 찍기
plt.scatter([3.0], [pred_tvEnd[0]], c='red', s=150, marker='*', label='3시간 예측값')

plt.xlabel('지상파 시청시간')
plt.ylabel('종편 시청 시간')
plt.legend()
plt.show()