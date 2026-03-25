# pandas의 DataFrame의 자료를 원격 DB의 테이블에 저장
# pip install sqlalchemy

import pandas as pd
from sqlalchemy import create_engine
import pymysql
try:
    data = {
    'code':[10,11,12],
    'sang':['사이다', '맥주', '와인'],
    'su':[20, 10, 5],
    'dan':['5000','3000','70000']
    }
    frame = pd.DataFrame(data)
    print(frame)

    engine = create_engine("mysql+pymysql://root:123@127.0.0.1:3306/test?charset=utf8")

    conn = engine.connect()
    # 저장
    frame.to_sql(name="sangdata", con=engine, if_exists='append', index=False)

    # 읽기
    df = pd.read_sql("select * from sangdata", engine)
    print(df)

except Exception as err:
    print("오류처리 : ", err)

"""
.env 파일
DB_USER=root
DB_PASS=123
from dotenv import load_dotenv
load_dotenv()

engine = create_engine(
    f"mysql+pymysql://{os.getenv('DB_USER')}:\
        {os.getenv('DB_PASS)}@127.0.0.1:3306/test?charset=utf8mb4"
)

"""