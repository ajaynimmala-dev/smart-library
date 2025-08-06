from flask import render_template,Blueprint

from database.models import User, db

user = Blueprint('users',__name__)

@user.route('/login')
def login():
    return render_template('login.html')

@user.route('/register')
def register():
    return render_template('register.html')

@user.route('/create')
def create():
    user = User()
    db.session.add(user)
    db.session.commit()
    return 'success'