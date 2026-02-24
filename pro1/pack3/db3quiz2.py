"""
문2) 직원번호와 직원명을 입력(로그인)하여 성공하면 아래의 내용 출력

직원번호 입력 : _______

직원명 입력 : _______

직원번호 직원명 부서명 부서전화 직급 성별

1 홍길동 총무부 111-1111 이사 남

...
"""

import MySQLdb

config = {
    'host' : '127.0.0.1',
    'user' : 'root',
    'password' : '123',
    'database' : 'test',
    'port' : 3306,
    'charset' : 'utf8'
}

def jikown() :
    try :
        conn = MySQLdb.connect(**config)   
        cursor = conn.cursor()
        
        jik_no = input('직원번호 입력 :')
        jik_name = input('직원명 입력 :')

        dsql ="""
        select jikwonno as 직원번호, jikwonname as 직원명, 
        busername as 부서명, busertel as 부서전화,
        jikwonjik as 직급, jikwongen as 성별
        from jikwon
        left outer join buser on busernum = buserno
        where jikwonno = '{0}' and jikwonname = '{1}'
        """.format(jik_no, jik_name)  


        cursor.execute(dsql)     
        
        check = cursor.fetchall()

        if len(check) == 0 :
            print("직원 정보가 없습니다.")
        else :
            for (jikwonno, jikwonname, busername, busertel, jikwonjik, jikwongen) in check :
                print(jikwonno, jikwonname, busername, busertel, jikwonjik, jikwongen)

    except Exception as e :
        print('err :', e)
    finally :
        cursor.close()
        conn.close()

if __name__ == "__main__" :
    jikown()