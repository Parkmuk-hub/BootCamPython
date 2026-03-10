from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# 메인 페이지
@app.route('/')
def index():
    return render_template('index.html')

# API 서버: 이름과 나이를 받아 연령대를 계산해줌
@app.route("/api/friend")
def api_friendFunc():
    name = request.args.get("name", "").strip()
    age_str = request.args.get("age", "").strip()
    
    # 필수 값 체크
    if not name:
        return jsonify({"ok": False, "error": "이름을 입력해주세요."}), 400
    if not age_str.isdigit():
        return jsonify({"ok": False, "error": "나이를 숫자로 정확히 입력해주세요."}), 400
    
    age = int(age_str)
    age_group = f"{(age // 10) * 10}대"

    # 결과 반환 (f-string 내 중괄호는 하나씩만!)
    return jsonify({
        "ok": True,
        "name": name,
        "age": age,
        "age_group": age_group,
        "message": f"{name}님은 {age}살 {age_group} 입니다."
    })

if __name__ == '__main__':
    app.run(debug=True)