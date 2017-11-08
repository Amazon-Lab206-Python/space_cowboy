from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "Secret"
mysql = MySQLConnector(app, 'emaildb')


@app.route('/')
def index():
    query = "SELECT * FROM email"
    emails = mysql.query_db(query)
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def create():
    query = "INSERT INTO email (email, created_at, updated_at) VALUES (:email, NOW(), NOW())"
    data = {
        'email': request.form['email']
    }
    mysql.query_db(query, data)
    query = "SELECT * FROM email"
    emails = mysql.query_db(query)
    return render_template('success.html', emails=emails)

@app.route('/success')
def success():
    query = "SELECT * FROM email"
    emails = mysql.query_db(query)
    return render_template('success.html', emails=email)


app.run(debug=True)
