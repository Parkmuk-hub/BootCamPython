# [로지스틱 분류분석 문제3]
# 얘를 사용해도 됨   'testdata/advertisement.csv' 
# 참여 칼럼 : 
#    - Daily Time Spent on Site : 사이트 이용 시간 (분)
#    - Age : 나이,
#    - Area Income : 지역 소득,
#    - Daily Internet Usage :일별 인터넷 사용량(분),
#    - Clicked Ad : 광고 클릭 여부 ( 0 : 클릭x , 1 : 클릭o )
# 광고를 클릭('Clicked on Ad')할 가능성이 높은 사용자 분류.
# 데이터 간 단위가 큰 경우 표준화 작업을 시도한다.
# 모델 성능 출력 : 정확도, 정밀도, 재현율, ROC 커브와 AUC 출력
# 새로운 데이터로 분류 작업을 진행해 본다.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, roc_curve, auc

# 1. 데이터 로드 및 전처리
df = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/advertisement.csv")
x = df[['Daily Time Spent on Site', 'Age', 'Area Income', 'Daily Internet Usage']]
y = df['Clicked on Ad']

# 2. 데이터 분리 및 스케일링
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

# 3. 모델 학습
model = LogisticRegression(C=10, solver='lbfgs', random_state=1)
model.fit(x_train, y_train)
y_train_hat = model.predict(x_train)
print('y_hat : ', y_train_hat[:5])        # y_hat :  [1 1 1 1 0]
print('real : ', y_train[:5])       # real : 0 1 0 1 1

f_value = model.decision_function(x_train)
print('f_value : ', f_value[:10])
print()
df = pd.DataFrame(np.vstack([f_value, y_train_hat, y_train]).T, columns=['f', 'y_train_hat', 'y_train'])
print(df.head())

from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_train, y_train_hat))

acc = (346 + 333) / 700       # TP + TN / 전체수  정확도
recall = 346 / (346 + 8)      # TP / (TP + FN)    재현율
precission = 346 / (346 + 13)  # TP / (TP + FP)    정밀도
specificity = 333 / (13 + 333)  # TN / (FP + TN)    특이도
fallout = 13 / (13 + 333)      # FP / (FP + TN)    위양성율

print('acc : ', acc)
print('recall : ', recall)      # tpr : 1에 근사하면 좋음
print('precission : ', precission)
print('specificity : ', specificity)
print('fallout : ', fallout)    # fpr : 0에 근사하면 좋음
print('fallout : ', 1 - specificity)
print()
from sklearn import metrics
acc_score = metrics.accuracy_score(y_train, y_train_hat)
print('모델 정확도 : ', acc_score)

cl_rep = metrics.classification_report(y_train, y_train_hat)
print(cl_rep)       # 종합 보고서?
print()

# 전체 x 대신 스케일링된 x_test(또는 x_train)를 사용해야 합니다.
# 여기서는 평가를 위해 x_test와 y_test를 사용하겠습니다.
y_train_score = model.decision_function(x_train)
fpr, tpr, thresholds = metrics.roc_curve(y_train, y_train_score)

plt.plot(fpr, tpr, 'o-', label='LogisticRegression')
plt.plot([0, 1],[0, 1], 'k--', label='random classifier line(AUC:0.5)')
# 위에서 계산한 fallout과 recall 점 찍기 (test 데이터 기준으로 다시 계산 필요)
plt.plot([fallout], [recall], 'ro', ms=6) 
plt.xlabel('FPR (1 - Specificity)')
plt.ylabel('TPR (Recall)')
plt.title('ROC Curve (Test Data)')
plt.legend()
plt.show()


print("AUC(Area Under the Curve) : ROC 커브의 면적. 1에 근사할수록 좋은 모델")
print("AUC : ", metrics.auc(fpr, tpr))  # AUC :  0.9931746187257111 좋은 모델이네!
