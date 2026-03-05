from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index() :
    return render_template("index.html");

@app.route("/condition")
def condition() :
    score = 85;
    return render_template("condition.html", score=score);

@app.route("/loop")
def loop() :
    users =["손오공", "진모리", "드래곤볼"];
    return render_template("loop.html", users=users);

@app.route("/filter")
def filter_ex() :
    message = "hello flask jinjsa2"
    price = 232323
    return render_template("filter.html", message=message, price=price)

if __name__ == '__main__' :
    app.run(debug=True)