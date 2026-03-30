# * 카이제곱 검정
# 카이제곱 문제1) 부모학력 수준이 자녀의 진학여부와 관련이 있는가?를 가설검정하시오
#   예제파일 : cleanDescriptive.csv
#   칼럼 중 level - 부모의 학력수준, pass - 자녀의 대학 진학여부
#   조건 :  level, pass에 대해 NA가 있는 행은 제외한다.

import pandas as pd
import scipy.stats as stats

# 데이터 로드
df = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/cleanDescriptive.csv")

# level, pass 열에 NA 행 제외
df_clean = df.dropna(subset=['level', 'pass'])

ctab = pd.crosstab(index=df_clean['level'], columns=df_clean['pass'])
print(ctab)

chi2, p= stats.chi2_contingency(ctab)

print(f"\n카이제곱: {chi2}")    # 카이제곱: 2.7669512025956684
print(f"p-value: {p}")          # p-value: 0.25070568406521365

if p < 0.05:
    print(f"판정: p-value({p}) < 0.05 이므로 귀무가설을 기각 => 통계적으로 유의미")
else:
    print(f"판정: p-value({p}) >= 0.05 이므로 귀무가설을 채택 => 통계적 관련 없음")