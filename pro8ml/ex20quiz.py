# [로지스틱 분류분석 문제2]
# 게임, TV 시청 데이터로 안경 착용 유무를 분류하시오.
# 안경 : 값0(착용X), 값1(착용O)
# 예제 파일 : https://github.com/pykwon  ==>  bodycheck.csv
# 새로운 데이터(키보드로 입력)로 분류 확인. 스케일링X

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import statsmodels.formula.api as smf

# 1. 데이터 로드
url = "https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/bodycheck.csv"
data = pd.read_csv(url)

# 2. 불필요한 컬럼 제거 (번호, 신장, 체중 제거)
data2 = data.drop(['번호', '신장', '체중'], axis=1)

# 3. 데이터 분리 (7:3 비율)
train, test = train_test_split(data2, test_size=0.3, random_state=42)

# 4. 모델 생성
# 컬럼 자동 선택 (안경유무 제외)
col_select = "+".join(train.columns.difference(['안경유무']))
my_formula = '안경유무 ~ ' + col_select

# [해결책] Singular matrix 에러 방지를 위해 method='bfgs'를 사용합니다.
# 이 알고리즘은 수렴 속도는 조금 느릴 수 있지만, 행렬 연산 에러에 훨씬 유연합니다.
model = smf.logit(formula=my_formula, data=train).fit(method='bfgs')

print(model.summary())

# 5. 테스트 데이터로 검증
pred_prob = model.predict(test)
# 0.5 기준으로 0과 1 분류 (np.rint 또는 np.where 사용)
y_pred = np.where(pred_prob >= 0.5, 1, 0)
y_true = test['안경유무'].values

print('\n[테스트 데이터 예측 결과]')
print('예측값 : ', y_pred[:10])
print('실제값 : ', y_true[:10])
print(f'정확도 : {accuracy_score(y_true, y_pred):.4f}')

# 6. 키보드로 새로운 데이터 입력받아 분류 (스케일링 X)
print('\n' + '='*40)
print('새로운 사용자의 안경 착용 유무 예측')
try:
    # 컬럼명 확인: CSV의 헤더가 '게임', 'TV시청'인지 확인 후 입력
    in_game = float(input("게임 시청 시간을 입력하세요: "))
    in_tv = float(input("TV 시청 시간을 입력하세요: "))

    # 입력받은 데이터를 학습 모델과 동일한 데이터프레임 형식으로 포장
    new_input = pd.DataFrame({'게임': [in_game], 'TV시청': [in_tv]})
    
    # 확률 예측
    new_prob = model.predict(new_input).values[0]
    
    # 결과 출력
    result_label = 1 if new_prob >= 0.5 else 0
    print("-" * 40)
    print(f"안경 착용 확률: {new_prob:.2f} ({round(new_prob * 100, 1)}%)")
    print(f"판정 결과: {'[안경 착용함]' if result_label == 1 else '[안경 미착용]'} ({result_label})")
    print('='*40)

except ValueError:
    print("숫자 형식으로 입력해 주세요.")
except Exception as e:
    print(f"오류 발생: {e}")

    # [로지스틱 분류분석 문제2] 
# 게임, TV 시청 데이터로 안경 착용 유무를 분류하시오.
# 안경 : 값0(착용X), 값1(착용O)
# 예제 파일 : https://github.com/pykwon  ==>  bodycheck.csv
# 새로운 데이터(키보드로 입력)로 분류 확인. 스케일링X
import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression


data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/fa236a226b6cf7ff7f61850d14f087ade1c437be/testdata_utf8/bodycheck.csv")

print(data.head(3))
#    번호  게임   신장  체중  TV시청  안경유무
# 0     1    2    146    34      2     0
# 1     2    6    169    57      3     1
# 2     3    9    160    48      3     1

# train/test set 분리
x = data[['게임','TV시청']]
y = data['안경유무']
# print(x[:3])
# print(y[:3])

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)
# print(x_train[:3], '\n', x_test[:3], '\n', y_train[:3], '\n', y_test[:3])
# -- x
#     게임  TV시청
# 11   5     3
# 3    1     2
# 18   1     1
#      게임  TV시청
# 0    2     2
# 17   8     2
# 15   5     3
# -- y
#  11    1
# 3     0
# 18    0
# Name: 안경유무, dtype: int64
#  0     0
# 17    1
# 15    1
# Name: 안경유무, dtype: int64

# 모델 생성
model = LogisticRegression(C=10, solver='lbfgs', random_state=1)
model.fit(x_train, y_train)

# 분류
y_pred = model.predict(x_test)
print("예측값: ", y_pred)
# 예측값:  [0 1 1 1 1 0]
print("실제값: \n", y_test)
# 실제값:  
# 0     0
# 17    1
# 15    1
# 1     1
# 8     1
# 5     0
# Name: 안경유무, dtype: int64

print(f"총 갯수: {len(y_test)}, 오류 수:{(y_test != y_pred).sum()}")
# 총 갯수: 6, 오류 수:0
print("--- 분류 정확도 확인 ---")
print(f"{accuracy_score(y_test, y_pred)}")

# 모델 저장 후 읽기
import joblib                           
joblib.dump(model, 'glasses.pkl')     
del model
read_model = joblib.load('glasses.pkl')

# 입력
game = float(input("게임 시간 입력: "))
tv = float(input("TV 시청 시간 입력: "))

new_data = pd.DataFrame([[game, tv]], columns=['게임', 'TV시청'])
new_pred = read_model.predict(new_data) 
print("안경 착용 여부: ", "착용" if new_pred[0] == 1 else "미착용")
print()           
print(f"안경 착용 확률: {read_model.predict_proba(new_data)[0][1]*100:.2f}%")