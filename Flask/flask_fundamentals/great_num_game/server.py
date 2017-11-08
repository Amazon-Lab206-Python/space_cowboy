from flask import Flask, render_template, request, redirect, session
import random
app= Flask(__name__)
app.secret_key = 'secretkey'

# @app.route('/')
# def index():
#     try:
#         session['winner']
#     except:
#         session['winner'] = random.randint(1,100)
#     return render_template('index.html')

# @app.route('/guess', methods=["POST"])
# def guess():
#     if (int(request.form['guess']) == session['winner']):
#         print: "You Win!"
#     elif (int(request.form['guess']) > session['winner']):
#         print "You're too high!"
#     else:
#         print "Down low, too slow"
#     return redirect ('/')


@app.route('/')
def root():
    session['x'] = random.randrange(0,101)
    return render_template('index.html', x = session['x'])

@app.route('/info', methods=["POST"])
def info():
    session['number'] = request.form['number']
    session['number'] = int(session['number'])
    print type(session['number'])
    return render_template('guess.html', x = session['x'], number = request.form['number'])

app.run(debug=True)