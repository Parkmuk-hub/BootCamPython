# 단일 모집단의 평균에 대한 가설검정 ( one samples t test)
# 실습 예제1
# A 중학교 1학년 1반 학생들의 시험결과가 담긴 파일을 읽어 처리
# 국어 점수 평균검정(80) studnet.csv

# 귀무(H0) : 학생들의 국어점수 평균은 80이 맞다.
# 대립(H1) : 학생들의 국어점수 평균은 80이 아니다.

import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import wilcoxon, shapiro



pd.set_option('display.max_columns', None)
data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/student.csv")
print(data.head(3))
print(data.describe())
print(data['국어'].mean())      # 72.9
print(len(data))        # 20 <= 제목 제외
# 30행이 넘으면 중심극한정리에 의해 정규성을 따른다고 가정
# 30개가 넘지 않으므로 정규성 검정 실시
print(stats.shapiro(data['국어']))  # pvalue=np.float64(0.01295975332132026)
# alpha 0.05 > pvalue 0.0129597 정규성 만족하지 않음
print()

# 정규성을 만족하지 못한 경우 대안
# Wilcoxon : 비모수 검정 방법으로 정규성이 없을 때 적절한 선택
wilcox_result = wilcoxon(data['국어'] - 80)
print("wilcox_result : ", wilcox_result)
# (statistic=np.float64(74.0), pvalue=np.float64(0.39777620658898905))
# alpha 0.05 < pvalue=0.3977762 이므로 귀무가설 채택
print()

result = stats.ttest_1samp(data['국어'], popmean=80)
print("result : ", result) 
# (statistic=np.float64(-1.3321801667713216), pvalue=np.float64(0.19856051824785262), df=np.int64(19)) 
# alpha 0.05 < pvalue=0.198560518 이므로 귀무가설 채택


# 결론 : 정규성은 부족하나 귀무가설 채택이라는 동일 결론을 얻음
# 표본 수가 크다면 그냥 ttest_1samp를 써도 된다.
# 보고서 작성 시에는 "shapiro-wilk 검정 결과 정규성 가성이 다소 위배되었으나
# 비모수 검정(wilcoxon) 결과도 동일하므로 ttest_1samp 결과를 신뢰할 수 있다" 라고 명시한다.

print('-----------------------------')
# 실습예제2
# 아이신생아 몸무게의 평균 검정 수행 babyboom.csv
# 아이신생아의 몸무게는 평균이 2800(g)으로 알려져 왔으나 이보다 더 크다는 주장이 나왔다.
# 표본으로 여아 18명을 뽑아 체중을 측정하였다고 할 때 새로운 주장이 맞는지 검정해보자

# 귀무 : 아이신생아의 몸무게는 평균이 2800(g)이다.
# 대립 : 아이신생아의 몸무게는 평균이 2800(g)보다 크다.

data2 = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/babyboom.csv")
print(data.head(3))
print(data.describe())
print()

fdata = data2[data2.gender == 1]    # 여아:1 / 남아:2
print(fdata, ' ', len(fdata))   # 18
print('여아 몸무게 평균 : ', np.mean(fdata.weight))     # 여아 몸무게 평균 :  3132.4444444444443
print('여아 몸무게 표준편차 : ', np.std(fdata['weight']))   # 여아 몸무게 표준편차 :  613.7878951616051
print()

# One-sample t-test
result2 = stats.ttest_1samp(fdata['weight'], popmean=2800)
print("result2 : ", result2)
#(statistic=np.float64(2.233187669387536), pvalue=np.float64(0.03926844173060218), df=np.int64(17)) 
# 해석1 (pvalue) : alpha 0.05 > pvalue=0.0392684이므로 귀무가설 기각
# 해석2 (t분포표) : t값 2.2331876, df 17, alpha 0.05, cv(임계값)? 1.740
# t값이 cv 값 오른쪽(귀무 기각영역)에 있으므로 귀무가설 기각

print("-------------------------------")
# 선행조건만 정규성 검정을 한 경우
print(stats.shapiro(fdata['weight'])) #  pvalue=0.01798478
# alpha 0.05 > pvalue=0.01798 정규성 만족하지 않음

# 정규성을 만족여부 시각화
sns.histplot(fdata['weight'], kde=True) # 왜곡된 데이터 분포를 확인
plt.show()

# 정규성을 만족여부 시각화 2 Quantile-Quantile plot
stats.probplot(fdata['weight'], plot=plt)   # Q-Q plot상에서 잔차가 정규성을 만족하지 못함
plt.show()

result3 = wilcoxon(fdata['weight'] - 2800)
print(result3)
# WilcoxonResult(statistic=np.float64(37.0), pvalue=np.float64(0.03423309326171875))
# 해석3 (wilcoxon p) : alpha 0.05 > pvalue 0.0342330 이므로 귀무가설 기각