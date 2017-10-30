from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def show_user_profile():
    return render_template("user.html")

@app.route('/ninjas')
def account():
    return render_template('ninja.html')

@app.route('/info', methods=['POST'])
def info():
    print request.form
    return 

app.run(debug=True) 