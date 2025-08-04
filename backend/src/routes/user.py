from flask import render_template,Blueprint

user = Blueprint('users',__name__)

@user.route('/login')
def login():
    return render_template('login.html')

@user.route('/register')
def register():
    return render_template('register.html')