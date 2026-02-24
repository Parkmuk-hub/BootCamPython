# 원격 데이터베이스 연동 프로그래밍
# MariaDB : driver file 설치 후 사용
# pip install Mysqlclient

import MySQLdb
"""
conn = MySQLdb.connect(
    host = '127.0.0.1',
    user = 'root',
    password = '123',
    database = 'test',
    port = 3306)
print(conn)
conn.close()
"""

# sangdata 자료 CRUD <select, insert, update, delete>
# config == dict값 저장
config = {
    'host' : '127.0.0.1',
    'user' : 'root',
    'password' : '123',
    'database' : 'test',
    'port' : 3306,
    'charset' : 'utf8'
}

def myFunc() :
    try:
        conn = MySQLdb.connect(**config)    # <== dict type == (**이름)
        cursor = conn.cursor()
        """
        # 자료 추가
        # isql = "insert into sangdata(code, sang, su, dan) values(5, '신상1', 5, 7800)"
        # cursor.execute(isql)
        # conn.commit() # 한번만 실행가능 

        isql = "insert into sangdata values(%s, %s, %s, %s)"
        # sql_data = (6, '신상2', 11 ,5000)
        sql_data = 6, '신상2', 11 ,5000
        cursor.execute(isql, sql_data)
        conn.commit()

        insert는 한번에 하나씩만 가능
        """

        # 자료 수정
        """        
        usql = "update sangdata set sang = %s, su = %s, dan = %s where code = %s "
        sql_data = ('물티슈', 66, 1000, 5)
        cursor.execute(usql, sql_data)
        conn.commit()
        """
        """
        usql = "update sangdata set sang = %s, su = %s, dan = %s where code = %s "
        sql_data = ('콜라', 77, 1000, 5)
        cou = cursor.execute(usql, sql_data) # 변수에 수정한 횟수를 리턴받아 출력할 수 있음
        print('수정 건수 :', cou)
        conn.commit()
        """

        # 자료 삭제
        code = '6'
        
        # dsql = "delete from sangdata where code =" + code   
        # sql 인젝션 공격을 받을 수 있음
        # 문자열 더하기로 sql 완성 비권장 - """secure coding 가이드라인""" 위배
        
        # 밑에 방법 둘다 굳!
        # dsql = "delete from sangdata where code = %s"
        # cursor.execute(dsql, (code,))
        
        dsql = "delete from sangdata where code ='{0}'".format(code)
        # cursor.execute(dsql)
        cou = cursor.execute(dsql)  # 삭제 후 반환 값 얻기 (0 또는 1 이상)
        if cou !=0 :
            print('삭제 성공!')
        else :
            print("삭제 실패;")
        conn.commit()


        # 자료 읽기
        sql = "select code, sang, su, dan from sangdata"
        cursor.execute(sql)
        for data in cursor.fetchall():
            # print(data)
            print('%s %s %s %s' %data)

        print()
        cursor.execute(sql)
        for r in cursor :
            print(r[0], r[1], r[2], r[3])

        print()
        cursor.execute(sql)
        for (code, sang, su, dan) in cursor :
            print(code, sang, su, dan)

        print()
        cursor.execute(sql)
        for (a, b, 수량, 단가) in cursor :      # 변수 이름 내맘대로 가능
            print(a, b, 수량, 단가)

    except Exception as e :
        print('err :', e)
        conn.rollback()
    finally :
        cursor.close()      # 생성 순서 역으로 close() 해줌
        conn.close()
        

if __name__ == "__main__" :
    myFunc()