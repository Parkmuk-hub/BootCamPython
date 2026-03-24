#  a) MariaDB에 저장된 jikwon, buser, gogek 테이블을 이용하여 아래의 문제에 답하시오.
#      - 사번 이름 부서명 연봉, 직급을 읽어 DataFrame을 작성
#      - DataFrame의 자료를 파일로 저장
#      - 부서명별 연봉의 합, 연봉의 최대/최소값을 출력
#      - 부서명, 직급으로 교차 테이블(빈도표)을 작성(crosstab(부서, 직급))
#      - 직원별 담당 고객자료(고객번호, 고객명, 고객전화)를 출력. 담당 고객이 없으면 "담당 고객  X"으로 표시
import sqlite3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib
import pymysql
import csv

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
    cursor = conn.cursor()
    sql = """
        select jikwonno,jikwonname,busername,jikwonpay,jikwonjik
        from jikwon inner join buser on jikwon.busernum = buser.buserno
    """
    cursor.execute(sql)
    rows = cursor.fetchall() 
    df1 = pd.DataFrame(rows, columns=['jikwonno','jikwonname','busername','jikwonpay','jikwonjik'])
    bn = df1.groupby('busername')['jikwonpay'].sum()
    print(bn)
    print("최대 연봉 : ", bn.max())
    print("최소 연봉 : ", bn.min())
    ctab = pd.crosstab(df1['busername'], df1['jikwonjik'])
    print(ctab)

    print()
    gsql = """
    select jikwonname, gogekno, gogekname, gogektel 
    from jikwon  
    left outer join gogek on jikwon.jikwonno = gogek.gogekdamsano
    order by jikwonname
    """
    cursor.execute(gsql)
    grow = cursor.fetchall()
    df2 = pd.DataFrame(grow, columns=['직원명', '고객번호', '고객명', '전화번호'])
    
    df2['고객번호'] = df2['고객번호'].fillna('담당 고객 X')
    df2['고객명'] = df2['고객명'].fillna('-')
    df2['전화번호'] = df2['전화번호'].fillna('-')
    print(df2)
#      - 연봉 상위 20% 직원 출력  : quantile()
#      - SQL로 1차 필터링 후 pandas로 분석 
#     - 조건: 연봉 상위 50% (df['연봉'].median() ) 만 가져오기  후 직급별 평균 연봉 출력
#      - 부서명별 연봉의 평균으로 가로 막대 그래프를 작성
except Exception as e:
    print("처리 오류 : ", e)
finally :
    cursor.close()
    conn.close()
#  b) MariaDB에 저장된 jikwon 테이블을 이용하여 아래의 문제에 답하시오.
#      - pivot_table을 사용하여 성별 연봉의 평균을 출력
#      - 성별(남, 여) 연봉의 평균으로 시각화 - 세로 막대 그래프
#      - 부서명, 성별로 교차 테이블을 작성 (crosstab(부서, 성별))
import sqlite3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib
import pymysql
import csv

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
    cursor = conn.cursor()
    sql = """
        select jikwongen, jikwonpay, busername from jikwon
        inner join buser on jikwon.busernum = buser.buserno
    """
    cursor.execute(sql)
    jrow = cursor.fetchall()
    df12 = pd.DataFrame(jrow, columns=['성별','연봉','부서명'])
    df_table = df12.pivot_table(index='성별', values='연봉', aggfunc='mean')
    print(df_table)

    df_table.plot(kind='bar', color=['skyblue', 'pink'], legend=False, rot=0)
    plt.title('성별 연봉 평균')
    plt.xlabel('성별')
    plt.ylabel('평균 연봉')
    plt.show()
    tab = pd.crosstab(df12['부서명'], df12['성별'])
    print(tab)
except Exception as e:
    print("처리 오류 : ", e)
finally :
    cursor.close()
    conn.close()
#  c) 키보드로 사번, 직원명을 입력받아 로그인에 성공하면 console에 아래와 같이 출력하시오.
#       조건 :  try ~ except MySQLdb.OperationalError as e:      사용
#      사번  직원명  부서명   직급  부서전화  성별
#      ...
#      인원수 : * 명
#     - 성별 연봉 분포 + 이상치 확인    <== 그래프 출력
#     - Histogram (분포 비교) : 남/여 연봉 분포 비교    <== 그래프 출력





# MariaDB에 저장된 jikwon, buser 테이블을 이용하여 아래의 문제에 답하시오.

# Django(Flask) 모듈을 사용하여 결과를 클라이언트 브라우저로 출력하시오.
#    1) 사번, 직원명, 부서명, 직급, 연봉, 근무년수를 DataFrame에 기억 후 출력하시오. (join)
#        : 부서번호, 직원명 순으로 오름 차순 정렬 
#    2) 부서명, 직급 자료를 이용하여  각각 연봉합, 연봉평균을 구하시오.
#    3) 부서명별 연봉합, 평균을 이용하여 세로막대 그래프를 출력하시오.
#    4) 성별, 직급별 빈도표를 출력하시오.


