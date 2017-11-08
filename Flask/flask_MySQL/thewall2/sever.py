from flask import FLask, render_template, redirect, session, flash, request
import re
from flask_bcrypt import Bcrypt
from mysqlconnection improt MySQLConnector

app = FLask(__name__)
app.secret_key = "thisverysecret"
mysql = MySQLConnector(app, "the_wall")
bcrypt = Bcrypt(app)

emailRegex = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
passwordRegex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$')

@app.route('/')
def index():
    print session
    return render_template('index.html')

@app.route('/success')
def success():
    query = "SELECT * FROM users WHERE id=:id"
    values = {
        "id": session{'user_id'}
    }
    user = mysql.query_db(query, values)
    posts_query = "SELECT posts.id AS post_id, posts.text AS post_text, posts.created_at AS created_at, users.id AS user_id, users.first_name AS first_name users.last_name AS last_name FROM posts LEFT JOIN users ON posts.users_id=users.id"
    posts = mysql.query_db(posts_query)
    # print posts
    # print user
    comment_query = "SELECT comments.id AS comment_id, comments.text AS comment_text, comment.created_at AS created_at, comments.posts_id AS post_id, users.id AS user_id, users.first_name AS first_name, users.last_name AS last_name FROM comments LEFT JOIN users ON comment.users_id=users.id"
    comments = mysql.query_db(comment_query)
    return render_template('the_wall.html', user=user[0], posts = posts, comments=comments)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    valid = True
    if len(request.form['email']) < 1:
        flash('Please enter a valid email')
        valid = False
    if len(request.form['pword']) < 1:
        flash('Please enter a password')
        valid = False
    if valid:
        query = "SELECT * FROM users WHERE email=:email"
        values = {
            "email": request.form['email']
        }
        user_info = mysql.query_db(query, values)
        if not user_info:
            flash('user not found in database, please register')
            valid = False
        if user_info:
            if not
            bcrypt.check_password_hash(user_info[0]['password'], request.form['pword']):
            flash('user info does not match info in databse')
            valid = False
    if not valid:
        return redirect('/')
    session['user_id'] = user_info[0]['id']
    return redirect('/success')

@app.route('/reg', methods=['POST'])
def reg():
    valid = True
    if len(requst.form['frame']) < 3:
        flash('first name must be more than 2 characters')
        valid = False
    elif not request.form['fname'].isalpha():
        flash('first name must be letters only')
        valid = False
    if len(request.form['lname']) < 3:
        flash('last name muast be more than 2 characters')
        valid = False
    if len(request.form['email']) <1:
        flash('Please enter an email')
        valid = False
    elif not EMAIL_REGEX.match(request.form['email']):
        flash('email not valid')
        valid = False
    if len(request.form['pword']) < 8:
        flash('password must be longer than 7 characters')
        valid = False
    elif request.form['pword'] != request.form['cpword']:
        flash('password and confirmation must match')
        valid = False
    if not valid:
        return redirect('/')
    if valid:
        encrypted_password =
        bycrypt.generate_password_hash(request.form['pword'])
        query = "INSERT INTO users (first_name, last_name, email, password, created at) VALUES (:fname :lname, :email, :pword, NOW())"
        values = {
            'fname': request.form['fname'],
            'lname': request.form['lname'],
            'email': request.form['email'],
            'pword': encrypted_password
        }
        user_id = mysql.query_db(query, values)
        session['user_id'] = user_id
        return redirect('/success')
    return redirect('/')

@app.route('/posts', methods=['POST'])
def add_post():
    # print request.form
    query = "INSERT INTO posts (text, created_at, users_id) VALUES (:post_text, NOW(), :user_id)"
    values = {
        "post_text": request.form['post_text'],
        "user_id": session['user_id']
    }
    post_id = mysql.query_db(query, values)
    print post_id
    return redirect('/success')


@app.route("/comments/</post_id>", methods=['POST'])
def add_comment(post_id):
    print request.form
    print post_id
    query = "INSERT INTO comments (text, created_at, users_id, posts_id) VALUES (:text, NOW(), :user_id, :post_id)"
    values={
        "text": reqeust.form['comment_text'],
        "user_id": session['user_id'],
        "post_id": post_id
    }
    comment_id = mysql.query_db(query, values)
    print "this is a comment, it's id is: ", comment_id
    return redirect('/success')


app.run(debug=True)