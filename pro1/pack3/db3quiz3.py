"""
문3) 성별 직원 현황 출력 : 성별(남/여) 단위로 직원 수와 평균 급여 출력

성별 직원수 평균급여

남 3 8500

여 2 7800
"""

import MySQLdb
import pickle

with open('mydb.dat', mode='rb') as obj :
    config = pickle.load(obj)

def genjik():
    try :
        conn = MySQLdb.connect(**config)
        cursor = conn.cursor()
        gsql ="""
        select jikwongen as 성별, count(*) as 직원수,
        round(avg(jikwonpay)) as 평균급여 from jikwon
        where jikwongen is not null
        group by jikwongen 
        """
        cursor.execute(gsql)
        gendata = cursor.fetchall()

        for gen, count, pay in gendata :
            print(gen, count, pay)
            
        

    except Exception as e :
        print('err :', e)
    finally :
        cursor.close()
        conn.close()


if __name__ == "__main__" :
    genjik()