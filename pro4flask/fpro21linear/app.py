from flask import Flask, render_template, request, jsonify
import pymysql
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from datetime import datetime

app = Flask(__name__)

# 전역 변수 초기화
model = None
r2 = 0
coef = 0
intercept = 0
jik_avg = []

def get_connection():
    return pymysql.connect(
        host='127.0.0.1', 
        user='root', 
        password='123', 
        database='test', 
        port=3306, 
        charset='utf8'
    )

def make_model():
    global model, r2, coef, intercept, jik_avg
    try:
        conn = get_connection()
        # 1. 학습용 데이터 로드
        query = "SELECT jikwonibsail, jikwonpay FROM jikwon"
        df = pd.read_sql(query, conn)
        
        # 2. 직급별 평균 데이터 로드
        avg_query = """
            SELECT IFNULL(jikwonjik, '직급없음') as jikwonjik, 
            ROUND(AVG(jikwonpay), 0) as avg_pay 
            FROM jikwon GROUP BY jikwonjik
        """
        avg_df = pd.read_sql(avg_query, conn)
        conn.close()

        # 데이터 가공 (안전하게 처리)
        df['jikwonibsail'] = pd.to_datetime(df['jikwonibsail'], errors='coerce')
        df = df.dropna(subset=['jikwonibsail', 'jikwonpay'])
        
        # 근무년수 계산 (현재 연도 기준)
        df['years'] = datetime.now().year - df['jikwonibsail'].dt.year
        df = df[df['years'] >= 0]

        if df.empty:
            print("경고: 학습할 데이터가 없습니다!")
            return

        # 모델 생성 및 학습
        x = df[['years']]
        y = df['jikwonpay']
        model = LinearRegression().fit(x, y)

        # 수치 저장
        coef = round(float(model.coef_[0]), 4)
        intercept = round(float(model.intercept_), 4)
        r2 = round(r2_score(y, model.predict(x)) * 100, 2)
        jik_avg = avg_df.to_dict(orient='records')
        
    except Exception as e:
        print(f"모델 생성 중 오류: {e}")

@app.route('/')
def index():
    if model is None: return "모델이 준비되지 않았습니다."
    
    # 초기값 (3년 기준) 예측
    test_df = pd.DataFrame({'years': [3]})
    pred = max(0, round(float(model.predict(test_df)[0]), 2))
    
    return render_template('index.html', pred=f"{pred:,.2f}", r2=r2, 
                           coef=coef, intercept=intercept, jik_avg=jik_avg)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        years = float(request.form.get('years', 3))
        
        # 예측 (반드시 학습할 때와 동일한 컬럼명을 가진 DataFrame 전달)
        test_df = pd.DataFrame({'years': [years]})
        pred_val = model.predict(test_df)[0]
        pred_res = max(0, round(float(pred_val), 2))

        return jsonify({
            'pred': f"{pred_res:,.2f}",
            'r2': r2,
            'coef': coef,
            'intercept': intercept
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    make_model()
    app.run(debug=True)