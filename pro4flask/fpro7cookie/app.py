from flask import Flask, render_template, request, make_response, redirect, url_for


app = Flask(__name__);
COOKIE_AGE = 60 * 60 * 24 * 7

@app.get("/")
def home() :
    return render_template("index.html");

@app.get("/login")
def loginfunc():
    # 쿠키에서 값을 가져오되, 없으면 None을 확실히 받음
    name = request.cookies.get("name")
    visits_cookie = request.cookies.get("visits")

    if name:
        # 로그인 상태인 경우
        visits = int(visits_cookie) + 1 if visits_cookie else 1
        msg = f"안녕하세요. {name}님 {visits}번째 방문입니다."
    else:
        # 로그아웃 상태인 경우
        visits = None
        msg = "이름을 입력하면 방문 횟수를 쿠키로 기억합니다."
    
    # 1. 먼저 템플릿을 렌더링한 응답 객체를 생성 (name 값이 정확히 넘어감)
    resp = make_response(render_template("login.html", msg=msg, name=name, visits=visits))

    # 2. 로그인 상태라면 브라우저의 visits 쿠키를 업데이트(갱신)
    if name:
        resp.set_cookie("visits", str(visits), max_age=COOKIE_AGE, samesite="LAX")

    return resp

@app.post("/login")
def loginfunc2():
    name = (request.form.get("name") or "").strip()

    resp = make_response(redirect(url_for("loginfunc")))

    resp.set_cookie("name", name, max_age=COOKIE_AGE, samesite="LAX")
    resp.set_cookie("visits", "0", max_age=COOKIE_AGE, samesite="LAX")
    return resp

@app.post("/logout")
def logoutfunc() :
    # 쿠키 삭제 후 /login(get)으로 이동
    resp = make_response(redirect(url_for("loginfunc")))
    resp.delete_cookie("name")
    resp.delete_cookie("visits")
    return resp

if __name__ == '__main__' :
    app.run(debug=True)