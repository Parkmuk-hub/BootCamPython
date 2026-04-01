print('two-sample t 검정 : 문제1') 
# 다음 데이터는 동일한 상품의 포장지 색상에 따른 매출액에 대한 자료이다. 
# 포장지 색상에 따른 제품의 매출액에 차이가 존재하는지 검정하시오.
"""
    귀무 : 포장지 색상에 따른 제품의 매출액에 차이가 없다
    대립 : 포장지 색상에 따른 제품의 매출액에 차이가 있다
"""
blue = [70, 68, 82, 78, 72, 68, 67, 68, 88, 60, 80]
red = [60, 65, 55, 58, 67, 59, 61, 68, 77, 66, 66]
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats
import koreanize_matplotlib

print(np.mean(blue) - np.mean(red)) # 8.999999999999993

# 시각화
# 1. np.arange(2)는 [0, 1]을 만듭니다.
x = np.arange(2)
# 2. 평균값을 리스트로 묶습니다.
means = [np.mean(blue), np.mean(red)]
# 3. 색상 이름을 리스트로 만듭니다. (파랑, 빨강 순서)
colors = ['blue', 'red']
# color 옵션에 리스트를 넣어주면 순서대로 적용됩니다.
plt.bar(x, means, color=colors, edgecolor='black', alpha=0.7) # 선명도(alpha)와 테두리(edgecolor) 추가
# x축 눈금 이름을 '파랑', '빨강'으로 바꿔주면 더 보기 좋습니다.
plt.xticks(x, ['파랑', '빨강'])
plt.xlim(-0.5, 1.5)
plt.xlabel('매출', fontdict={'fontsize':12, 'fontweight':'bold'})
plt.show()

# 정규성 검정
print(stats.shapiro(blue))      # 0.510231 > 0.05 만족하여 모수 검정
print(stats.shapiro(red))       # 0.534793 > 0.05
print()

# 독립표본 검정
result1 = stats.ttest_ind(blue, red, equal_var=True)
print(result1)
# TtestResult : statistic=2.9280203, pvalue=0.008316545, df=20
# 해석 : pvalue 0.008316545 < alpha 0.05 이므로 귀무가설 기각
# 포장지 색상에 따른 제품의 매출액에 차이가 있다. 라는 의견을 받아 들임
print()

print('two-sample t 검정 : 문제2')  
# 아래와 같은 자료 중에서 남자와 여자를 각각 15명씩 무작위로 비복원 추출하여 
# 혈관 내의 콜레스테롤 양에 차이가 있는지를 검정하시오.
"""
    귀무 : 남녀 혈관 내의 콜레스테롤 양에 차이가 없다.
    대립 : 남녀 혈관 내의 콜레스테롤 양에 차이가 있다.
"""
man =  [0.9, 2.2, 1.6, 2.8, 4.2, 3.7, 2.6, 2.9, 3.3, 1.2, 3.2, 2.7, 3.8, 4.5, 4, 2.2, 0.8, 0.5, 0.3, 5.3, 5.7, 2.3, 9.8]
woman = [1.4, 2.7, 2.1, 1.8, 3.3, 3.2, 1.6, 1.9, 2.3, 2.5, 2.3, 1.4, 2.6, 3.5, 2.1, 6.6, 7.7, 8.8, 6.6, 6.4]

print(np.mean(man) - np.mean(woman))    # -0.4747826086956528 여자 쪽이 더 큼

# 시각화
# 1. np.arange(2)는 [0, 1]을 만듭니다.
y = np.arange(2)
# 2. 평균값을 리스트로 묶습니다.
means = [np.mean(man), np.mean(woman)]
# 3. 색상 이름을 리스트로 만듭니다. (파랑, 빨강 순서)
colors = ['skyblue', 'pink']
# color 옵션에 리스트를 넣어주면 순서대로 적용됩니다.
plt.bar(y, means, color=colors, edgecolor='black', alpha=0.7) # 선명도(alpha)와 테두리(edgecolor) 추가
# x축 눈금 이름을 '파랑', '빨강'으로 바꿔주면 더 보기 좋습니다.
plt.xticks(y, ['남자', '여자'])
plt.xlim(-0.5, 1.5)
plt.xlabel('콜레스테롤 양', fontdict={'fontsize':12, 'fontweight':'bold'})
plt.show()

# 정규성 검정
print(stats.shapiro(man))   # 0.01670927 < 0.05 정규성 불만족
print(stats.shapiro(woman)) # 0.00080136 < 0.05
print()

# 비모수 검정
result2 = stats.mannwhitneyu(man, woman)
print(result2)
# MannwhitneyuResult : statistic=221.5, pvalue=0.8454793
# 해석 : pvalue 0.8454793 > alpha 0.05 이므로 귀무가설 채택
# 남녀 혈관 내의 콜레스테롤 양에 차이가 없다. 라는 의견을 받아 들임

print('two-sample t 검정 : 문제3')
# DB에 저장된 jikwon 테이블에서 총무부, 영업부 직원의 연봉의 평균에 차이가 존재하는지 검정하시오.
# 연봉이 없는 직원은 해당 부서의 평균연봉으로 채워준다.
"""
    귀무 : 총무부, 영업부 직원의 연봉 평균에 차이가 없다.
    대립 : 총무부, 영업부 직원의 연봉 평균에 차이가 있다.
"""
import os 
import pymysql
import pandas as pd
config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database':'test',
    'port':3306,    
    'charset':'utf8'
}
try :
    conn = pymysql.connect(**config)
    # conn = sqlite3.connect(**config)
    cursor = conn.cursor()
    sql = """
        select busername, jikwonpay
        from jikwon inner join buser on jikwon.busernum = buser.buserno
        WHERE busername IN ('총무부', '영업부')
    """
    cursor.execute(sql)
    rows = cursor.fetchall() 
    # 1. 데이터프레임 만들기
    df = pd.DataFrame(rows, columns=['busername', 'jikwonpay'])

    # 2. 연봉 결측치(None) 채우기 (해당 부서의 평균으로!)
    # SQL에서 가져올 때 연봉이 없으면 None으로 들어옵니다.
    df['jikwonpay'] = df['jikwonpay'].fillna(df.groupby('busername')['jikwonpay'].transform('mean'))

    # 3. 부서별로 쪼개기
    chongmu = df[df['busername'] == '총무부']['jikwonpay']
    youngup = df[df['busername'] == '영업부']['jikwonpay']
    # 정규성 검정
    print(stats.shapiro(chongmu))   # 0.0260449 < 0.05  정규성 불만족
    print(stats.shapiro(youngup))   # 0.0256083 < 0.05
    print()
    
    # 비모수 검정
    result3 = stats.mannwhitneyu(chongmu, youngup)
    print(result3)
    # MannwhitneyuResult : statistic=51.0, pvalue=0.47213346
    # 해석 : pvalue 0.47213346 > alpha 0.05 귀무가설 채택
    # 총무부, 영업부 직원의 연봉 평균에 차이가 없다. 라는 의견을 받아 들임
finally :
    conn.close()
print()

print('대응표본 t 검정 : 문제4')
# 어느 학급의 교사는 매년 학기 내 치뤄지는 시험성적의 결과가 실력의 차이없이 비슷하게 유지되고 있다고 말하고 있다. 
# 이 때, 올해의 해당 학급의 중간고사 성적과 기말고사 성적은 다음과 같다. 
# 점수는 학생 번호 순으로 배열되어 있다.
"""
    귀무 : 중간고사 성적과 기말고사 성적은 차이가 없다.
    가설 : 중간고사 성적과 기말고사 성적은 차이가 있다.
"""
mid = [80, 75, 85, 50, 60, 75, 45, 70, 90, 95, 85, 80]
final = [90, 70, 90, 65, 80, 85, 65, 75, 80, 90, 95, 95]

print(np.mean(mid) - np.mean(final))    # -7.5 차이가 있는듯?

# 시각화
# 1. np.arange(2)는 [0, 1]을 만듭니다.
z = np.arange(2)
# 2. 평균값을 리스트로 묶습니다.
means = [np.mean(mid), np.mean(final)]
# 3. 색상 이름을 리스트로 만듭니다. (파랑, 빨강 순서)
colors = ['orange', 'red']
# color 옵션에 리스트를 넣어주면 순서대로 적용됩니다.
plt.bar(z, means, color=colors, edgecolor='black', alpha=0.7) # 선명도(alpha)와 테두리(edgecolor) 추가
# x축 눈금 이름을 '파랑', '빨강'으로 바꿔주면 더 보기 좋습니다.
plt.xticks(z, ['중간고사', '기말고사'])
plt.xlim(-0.5, 1.5)
plt.xlabel('시험성적', fontdict={'fontsize':12, 'fontweight':'bold'})
plt.show()

# 정규성 검정
print(stats.shapiro(mid))   # 0.368147 > 0.05 정규성 만족
print(stats.shapiro(final)) # 0.193002 > 0.05 
print()

result4 = stats.ttest_rel(mid, final)
print(result4)
# TtestResult : statistic=-2.6281127, pvalue=0.0234861, df=11
# 해석 : pvalue 0.0234861 < alpha 0.05 이므로 귀무가설 기각
# 중간고사 성적과 기말고사 성적은 차이가 있다. 라는 의견을 받아 들임