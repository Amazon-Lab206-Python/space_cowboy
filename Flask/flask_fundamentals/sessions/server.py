from flask import Flask, render_template, request, session, redirect
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/info", methods=["POST"])
def info():
    session['first_name'] = request.form['first_name']
    print session['first_name']
    return redirect('/result')


@app.route('/result')
def result():
    return render_template('result.html')


app.run(debug=True)
