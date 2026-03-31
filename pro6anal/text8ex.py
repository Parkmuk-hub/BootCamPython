import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import wilcoxon, shapiro
import koreanize_matplotlib
print('one-sample t 검정 : 문제1')  
# 영사기( 프로젝터 )에 사용되는 구형 백열전구의 수명은 250 시간이라고 알려졌다. 
# 한국 연구소에서 수명이 50 시간 더 긴 새로운 백열전구를 개발하였다고 발표하였다. 
# 연구소의 발표결과가 맞는지 새로 개발된 백열전구를 임의로 수집하여 수명 시간 관련 자료를 얻었다. 
# 한국 연구소의 발표가 맞는지 새로운 백열전구의 수명을 분석하라.
# 수집된 자료 :  305 280 296 313 287 240 259 266 318 280 325 295 315 278

"""
    문제 : 새로 개발된 백열전구의 평균 수명이 300시간인지 검정
    귀무 : 새 전구의 평균 수명은 300시간이다.
    대립 : 새 전구의 평균 수명은 300시간이 아니다.
"""

data = [305, 280, 296, 313, 287, 240, 259, 266, 318, 280, 325, 295, 315, 278]
df = pd.DataFrame(data=data, columns=['수명시간'])
print("평균 수명시간 : ",df['수명시간'].mean())
v_result = shapiro(df['수명시간'])  # 289.7857142857143
print(v_result)
# ShapiroResult : statistic=0.966114, pvalue=0.820861
# 해석 1 (p) : alpha 0.05 < pvalue=0.820861이므로 귀무가설 채택
t1_result = stats.ttest_1samp(df['수명시간'], popmean=300)
print(t1_result)
# TtestResultstatistic : statistic=-1.5564356, pvalue=0.1436062, df=13
# 해석 2 : alpha 0.05 < pvalue=0.1436062 이므로 귀무가설 채택
# print()
# print('표본 평균 수명 시간 :', np.mean(data))
# print('표본 크기 :', len(data))



print('one-sample t 검정 : 문제2')
# 국내에서 생산된 대다수의 노트북 평균 사용 시간이 5.2 시간으로 파악되었다.
#  A회사에서 생산된 노트북 평균시간과 차이가 있는지를 검정하기 위해서 
# A회사 노트북 150대를 랜덤하게 선정하여 검정을 실시한다.  
# 실습 파일 : one_sample.csv
# 참고 : time에 공백을 제거할 땐 ***.time.replace("     ", ""),
#           null인 관찰값은 제거.

"""
    문제 : 국내 노트북 평균 사용 시간인 5.2시간과 A사 노트북의 평균 사용 시간에 차이가 있는지 검정
    귀무 : A회사 노트북의 평균 사용 시간은 5.2시간이다. (차이가 없다.)
    대립 : A회사 노트북의 평균 사용 시간은 5.2시간이 아니다. (차이가 있다.)
"""

df1 = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/one_sample.csv")
# print(df1)
df1_t = pd.to_numeric(df1.time.str.replace("time", ""), errors='coerce')
print('평균 사용시간 : ',df1_t.mean()) # 5.556880733944954
t_result = shapiro(df1_t.dropna())
print(t_result)
# ShapiroResult : statistic=0.9913731, pvalue=0.7242303
# 해석 1 (p) : alpha 0.05 < pvalue=0.7242303 이므로 귀무가설 채택
t2_result = stats.ttest_1samp(df1_t.dropna(), popmean=5.2)
print(t2_result)
# TtestResult : statistic=3.94605956, pvalue=0.00014166691, df=108
# 해석 2 : alpha 0.05 > pvalue=0.00014166 이므로 귀무가설 기각
print()

data2 = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/one_sample.csv")

# # 전처리
# data2['time'] = data2['time'].replace("     ", "").str.strip() # 공백 제거
# data2['time'] = pd.to_numeric(data2['time'], errors='coerce')  # 숫자 변환
# data2 = data2.dropna(subset=['time'])  # null인 관찰값 제거

# print('표본 평균 사용 시간 :', data2['time'].mean())
# print('표본 크기 :', len(data2))


print('one-sample t 검정 : 문제3')
# https://www.price.go.kr/tprice/portal/main/main.do 에서 
# 메뉴 중  가격동향 -> 개인서비스요금 -> 조회유형:지역별, 품목:미용 자료(엑셀)를 파일로 받아 
# 미용 요금을 얻도록 하자. 
# 정부에서는 전국 평균 미용 요금이 15000원이라고 발표하였다. 이 발표가 맞는지 검정하시오. (월별)

"""
    문제 : 정부의 전국 평균 미용 요금 15,000원이 실제 데이터와 차이가 있는지 검정
    귀무 : 전국 평균 미용 요금은 15,000원이다. (발표가 맞다.)
    대립 : 전국 평균 미용 요금은 15,000원이 아니다. (발표가 틀리다.)
"""

df2 = pd.read_excel("가격동향.xls")

df3 = df2.iloc[0, 2:]
df3 = pd.to_numeric(df3, errors='coerce')
df3 = df3.dropna()

print("평균 미용 요금 : ", df3.mean())  # 20003.9375
print("표본 크기 : ", len(df3)) # 16

p_result = shapiro(df3)
print(p_result)
# ShapiroResult : statistic=0.90244432, pvalue=0.0879570671

pt_result = stats.ttest_1samp(df3, popmean=15000)
print(pt_result)
# TtestResult : statistic=7.17436, pvalue=3.20576619, df=15