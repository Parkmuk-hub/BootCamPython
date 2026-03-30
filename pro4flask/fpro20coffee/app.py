from pathlib import Path
from flask import Flask, render_template, request, redirect, url_for
from db import insert_survey, fetchall_survey
from analysis import analysiy_func, save_bar_chart_func

BASE_DIR = Path(__file__).resolve().parent
IMG_PATH = BASE_DIR / 'static' / 'images' / 'vbar.png'

app = Flask(__name__)

@app.get("/")
def index():
    return render_template('index.html')

@app.get("/coffee/survey")
def survey_view() :
    return render_template('coffee/coffeesurvey.html')

@app.post("/coffee/surveyprocess")
def surveyprocess() :
    gender = request.form.get('gender', "").strip()
    age_raw = request.form.get('age', "").strip()
    co_survey = request.form.get('co_survey', "").strip()

    # age_raw는 "20대" 같은 문자열이므로 .isdigit()를 빼야 통과됩니다.
    if not gender or not co_survey or not age_raw:
        return redirect(url_for('survey_view'))
    
    # DB 저장 (age_raw를 그대로 저장하거나, 필요시 전처리)
    insert_survey(gender=gender, age=age_raw, co_survey=co_survey)

    rdata = fetchall_survey()
    crossTab, results, df = analysiy_func(rdata)

    # 차트 저장
    if not df.empty:
        save_bar_chart_func(df, IMG_PATH)

    # render_template 따옴표 오타도 수정
    return render_template("coffee/result.html", 
                        crossTab=crossTab.to_html() if not crossTab.empty else "데이터가 없어요",
                        results=results,
                        df=df.to_html(index=False) if not df.empty else "")

@app.get("/coffee/surveyshow")
def survey_show() :
    # 저장 없이 결과만 출력
    rdata = fetchall_survey()
    crossTab, results, df = analysiy_func(rdata)

    # 차트 저장
    if not df.empty:
        save_bar_chart_func(df, IMG_PATH)

    # render_template 따옴표 오타도 수정
    return render_template("coffee/result.html", 
                        crossTab=crossTab.to_html() if not crossTab.empty else "데이터가 없어요",
                        results=results,
                        df=df.to_html(index=False) if not df.empty else "")

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5000)