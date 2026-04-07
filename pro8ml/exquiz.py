print('[로지스틱 분류분석 문제1]')
# 문1] 소득 수준에 따른 외식 성향을 나타내고 있다. 주말 저녁에 외식을 하면 1, 외식을 하지 않으면 0으로 처리되었다. 
# 다음 데이터에 대하여 소득 수준이 외식에 영향을 미치는지 로지스틱 회귀분석을 실시하라.
# 키보드로 소득 수준(양의 정수)을 입력하면 외식 여부 분류 결과 출력하라.
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf

df = pd.read_csv("outdin.csv")
# print(df)
#    요일  외식유무  소득수준
print(df['외식유무'].unique())

# ======================================
# 모델 작성 방법 1 : logit()  사용
# ======================================
formula = '외식유무 ~ 요일 + 소득수준' 
result = smf.logit(formula=formula, data=df).fit()
print(result.summary())    # Logit Regression Results

pred = result.predict(df[:10])  
print('\n 예측값 : ', np.round(pred.values)) # np,.round() 0.5를 기준으로 반올림하여 0 또는 1로 분류함
#  예측값 :  [1. 0. 0. 1. 0. 1. 1. 1. 0. 0.]
print('\n 실제값 : ', df['외식유무'][:10].values)
# 실제값 :  [0 0 0 1 0 1 1 1 0 0]
# [분석 결과]
# - 정답(True): 10개 중 9개 맞춤 (정확도 Accuracy: 90%)
# - 오류(Error): 1개 틀림 (실제 0인데 1으로 예측: 1개)
print()
print('수치에 대한 집계표(Confusion matrix, 혼돈행렬) 확인 ---')
conf_tab = result.pred_table()
print(conf_tab)
# [[12.  1.]
#  [ 1. 14.]]

# # 현재 모델의 분류 정확도 확인 1 - Confusion matrix 이용
# print('분류 정확도 : ', (12 + 14)/len(df))
# print('분류 정확도 : ', (conf_tab[0][0] + conf_tab[1][1]) / len(df))

# 모듈로 확인 2 : accuacy_score 이용
from sklearn.metrics import accuracy_score
pred2 = result.predict(df)
print('분류 정확도 : ', accuracy_score(df['외식유무'], np.around(pred2)))

import statsmodels.api as sm
print('*' * 10)
# 모델 작성 방법 2 : glm() - 일반화된 선형모델
result2 = smf.glm(formula=formula, data=df, family=sm.families.Binomial()).fit()
# Binomial() : 이항분포, Gaucian : 정규분포 - 기본값
print(result2.summary())

glm_pred2 = result2.predict(df)
print('glm 모델 분류 정확도 : ', accuracy_score(df['외식유무'], np.around(glm_pred2)))
print("\n" + "="*30)
try:
    # 1. 요일 입력받기 (예: 토, 일, 월...)
    user_day = input("요일을 입력해주세요 (토/일/월/화/수/목/금): ").strip()
    
    # 2. 소득 수준 입력받기
    user_income = int(input("소득 수준을 입력해주세요 (양의 정수): "))

    # 3. 모델이 읽을 수 있게 데이터프레임으로 만들기 (컬럼명이 중요!)
    # 학습할 때 썼던 '요일', '소득수준'이라는 이름을 똑같이 써야 합니다.
    new_input_df = pd.DataFrame({
        '요일': [user_day], 
        '소득수준': [user_income]
    })

    # 4. 예측하기
    # result는 아까 smf.logit().fit()으로 만든 결과 객체입니다.
    pred_prob = result.predict(new_input_df).values[0]

    # 5. 결과 출력
    print("\n" + "="*40)
    print(f"[{user_day}요일 / 소득 {user_income}] 예측 결과")
    print(f"외식 확률: {pred_prob:.2f} ({round(pred_prob * 100, 1)}%)")
    
    if pred_prob >= 0.5:
        print("결과: 외식을 할 가능성이 높습니다! (1)")
    else:
        print("결과: 외식을 하지 않을 가능성이 높습니다. (0)")
    print("="*40)

except ValueError:
    print("소득 수준은 숫자로 입력해 주세요!")
except Exception as e:
    print(f"오류가 발생했습니다: {e}")
    print("데이터에 있는 요일(토, 일, 월, 화, 수, 목, 금)을 정확히 입력했는지 확인하세요.")