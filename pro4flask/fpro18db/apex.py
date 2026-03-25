from flask import Flask, render_template, request
import pymysql
import pandas as pd
import numpy as np
from markupsafe import escape
import matplotlib.pyplot as plt
import koreanize_matplotlib 
import os

app = Flask(__name__)

db_config = {
    'host':'127.0.0.1', 'user':'root', 'password':'123',
    'database':'test','port':3306,'charset':'utf8mb4'
}

def get_connection() :
    return pymysql.connect(**db_config)

@app.route("/")
def index() :
    return render_template("home.html")

@app.route("/dbjik")
def dbjik():

    conn = get_connection() 
    
    try:

        with conn.cursor() as cursor:
            sql = """
                select jikwonno, jikwonname, busername, jikwonjik, jikwonpay, (YEAR(NOW()) - YEAR(jikwonibsail))as jikgn, jikwongen
                from jikwon 
                inner join buser on busernum = buserno
                order by busernum, jikwonname asc
            """
            cursor.execute(sql)
            rows = cursor.fetchall() 
            

            df = pd.DataFrame(rows, columns=['사번','직원명','부서명','직급','연봉','근무년수', '성별'])
            
            df_t = df.to_html(classes='table', index=False)

            dfsm = df.groupby('부서명')['연봉'].agg(['sum', 'mean']).reset_index().round(2)
            dfsm.columns = ['부서명', '연봉합', '연봉평균']
            df_s = dfsm.to_html(classes='table', index=False)

            fig, axes = plt.subplots(1, 2, figsize=(12, 5))
            
            dfsm.plot(kind='bar', x='부서명', y='연봉합', ax=axes[0], color='skyblue', rot=0)
            axes[0].set_title('부서별 연봉 합계')

            dfsm.plot(kind='bar', x='부서명', y='연봉평균', ax=axes[1], color='orange', rot=0)
            axes[1].set_title('부서별 연봉 평균')

            plt.tight_layout()

            static_path = os.path.join(app.root_path, 'static')
            chart_path = os.path.join(static_path, 'result_chart.png')
            plt.savefig(chart_path)

            ctab1 = pd.crosstab(df['성별'], df['직급']).reset_index()
            ctab = ctab1.to_html(classes='table', index=False)

            dfmax = df.groupby('부서명')['연봉'].agg(['max']).reset_index()
            dfmax.columns = ['부서명', '연봉']
            dfmax_p = pd.merge(df, dfmax, on=['부서명', '연봉'])
            dfmax_p = dfmax_p[['부서명', '직원명', '연봉']]
            dfmp_t = dfmax_p.to_html(classes='table', index=False)

            dfcount_b = df['부서명'].value_counts()
            total = len(df)
            dfcount = (dfcount_b / total * 100).round(2).reset_index()
            dfcount.columns = ['부서명', '비율(%)']
            total_t = (f"총 인원 : {total}명")
            dfcount_t = dfcount.to_html(classes='table', index=False) 




            return render_template("dbjik.html", df_t=df_t,df_s=df_s, chart_url='/static/result_chart.png', ctab=ctab, dfmp_t=dfmp_t,
                                total_t=total_t,dfcount_t=dfcount_t)
            
    finally:

        conn.close()


if __name__ == '__main__' :
    app.run(debug=True)