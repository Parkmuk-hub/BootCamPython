import os
import pymysql

def get_conn() :
    return pymysql.connect(
        host=os.getenv('DB_HOST', '127.0.0.1'),
        port=int(os.getenv('DB_PORT', 3306)),
        user=os.getenv('DB_USER', 'root'),
        password=os.getenv('DB_PASSWORD', '123'),
        db=os.getenv('DB_NAME', 'test'),
        charset='utf8mb4',        
        cursorclass=pymysql.cursors.DictCursor,
        autocommit=True
    )