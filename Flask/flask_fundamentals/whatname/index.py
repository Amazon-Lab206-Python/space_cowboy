from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def show_user_profile():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def account():
    print request.form
    return render_template('/index.html')


app.run(debug=True)