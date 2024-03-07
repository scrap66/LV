from flask import Flask, render_template

app =Flask(__name__)


@app.route("/")
def index():
    return render_template('main.html')

@app.route("/photoalbum")
def photo():
    return render_template('photoalbum.html')

@app.route("/survey")
def survey():
    return render_template('survey.html')

@app.route("/arts")
def arts():
    return render_template('arts.html')

if __name__ == "__main__":
    app.run(debug=False)