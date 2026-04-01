# 빵을 기름에 튀길 때 네 가지 기름의 종류에 따라 빵에 흡수된 기름의 양을 측정하였다.

# 기름의 종류에 따라 흡수하는 기름의 평균에 차이가 존재하는지를 분산분석을 통해 알아보자.

# 조건 : NaN이 들어 있는 행은 해당 칼럼의 평균값으로 대체하여 사용한다.
"""
    귀무 : 기름의 종류에 따라 흡수하는 기름의 평균에 차이가 없다
    대립 : 기름의 종류에 따라 흡수하는 기름의 평균에 차이가 있다
"""
import pandas as pd
import numpy as np
from scipy import stats
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
import matplotlib.pyplot as plt
import koreanize_matplotlib
# 데이터 생성
data = {
    'kind': [1, 2, 3, 4, 2, 1, 3, 4, 2, 1, 2, 3, 4, 1, 2, 1, 1, 3, 4, 2],
    'quantity': [64, 72, 68, 77, 56, np.nan, 95, 78, 55, 91, 63, 49, 70, 80, 90, 33, 44, 55, 66, 77]
}
df = pd.DataFrame(data)
df['quantity'] = df['quantity'].fillna(df['quantity'].mean())
gr1 = df[df['kind'] == 1]['quantity']
gr2 = df[df['kind'] == 2]['quantity']
gr3 = df[df['kind'] == 3]['quantity']
gr4 = df[df['kind'] == 4]['quantity']
print(gr1, ' ', np.mean(gr1))   # 63.25438596491228
print(gr2, ' ', np.mean(gr2))   # 68.83333333333333
print(gr3, ' ', np.mean(gr3))   # 66.75
print(gr4, ' ', np.mean(gr4))   # 72.75
print()

# 정규성 검정
print(stats.shapiro(gr1).pvalue)    # 0.8680405840743664 > 0.05 만족
print(stats.shapiro(gr2).pvalue)    # 0.5923924912154501
print(stats.shapiro(gr3).pvalue)    # 0.48601083943678747
print(stats.shapiro(gr4).pvalue)    # 0.48601083943678747
print()

# 등분산성
print(stats.levene(gr1, gr2, gr3, gr4).pvalue)      # 0.3268969935062273 > 0.05 만족
print(stats.bartlett(gr1, gr2, gr3, gr4).pvalue)    # 0.19342011099507922

lmodel = ols('quantity ~ C(kind)', data=df).fit()   # C(group)은 범주형
print(anova_lm(lmodel, typ=1))
#             df       sum_sq     mean_sq         F    PR(>F)
# C(kind)    3.0   231.304247   77.101416  0.266935  0.848244
# Residual  16.0  4621.432595  288.839537       NaN       NaN
# 해석 : pvalue 0.848244 > 0.05 이므로 귀무가설 채택
# 기름의 종류에 따라 흡수하는 기름의 평균에 차이가 없다

# 사후 검정
from statsmodels.stats.multicomp import pairwise_tukeyhsd
tukResult = pairwise_tukeyhsd(endog=df.quantity, groups=df.kind)
print(tukResult)

# 시각화
tukResult.plot_simultaneous(xlabel='mean', ylabel='group')
plt.show()

print('ANOVA 예제 2')
# DB에 저장된 buser와 jikwon 테이블을 이용하여 총무부, 영업부, 전산부, 관리부 직원의 
# 연봉의 평균에 차이가 있는지 검정하시오. 
# 만약에 연봉이 없는 직원이 있다면 작업에서 제외한다.
import os 
import pymysql
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
        order by jikwonpay is not null
    """
    cursor.execute(sql)
    rows = cursor.fetchall() 
    df = pd.DataFrame(rows, columns=['busername', 'jikwonpay'])
    print(df)
    ch = df[df['busername'] == '총무부']['jikwonpay']
    gw = df[df['busername'] == '관리부']['jikwonpay']
    yo = df[df['busername'] == '영업부']['jikwonpay']
    je = df[df['busername'] == '전산부']['jikwonpay']

    # 정규성 검정
    print(stats.shapiro(ch).pvalue)     # 0.026044936412817302
    print(stats.shapiro(gw).pvalue)     # 0.9078027897950541
    print(stats.shapiro(yo).pvalue)     # 0.02560839951152337
    print(stats.shapiro(je).pvalue)     # 0.4194072051776978
    print()

    # 등분산성
    print(stats.levene(ch, gw, yo, je))
    # LeveneResult : statistic(0.3378755, pvalue=0.7980753
    # 해석 : p > a 이므로 귀무가설 채택

    # 정규성 X, 등분산성 O => kruskal()
    print()
    print(stats.kruskal(ch, gw, yo, je).pvalue)
    # 0.6433438752252685 > a 이므로 귀무 채택
    print()

    # 사후 검정
    from statsmodels.stats.multicomp import pairwise_tukeyhsd
    tukResult = pairwise_tukeyhsd(endog=df.jikwonpay, groups=df.busername)
    print(tukResult)

    # 시각화
    tukResult.plot_simultaneous(xlabel='mean', ylabel='group')
    plt.show()



finally :
    conn.close()