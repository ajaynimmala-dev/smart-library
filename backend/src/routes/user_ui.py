from flask import render_template, Blueprint, request, redirect, url_for, flash, jsonify

from random import randint

from flask_login import current_user

from database.models import User, db

user = Blueprint('users', __name__)

dashboard_keys = {
    "55":1
}


@user.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        if request.form:
            form = request.form
            user_email = form.get("email")
            user_pass = form.get("password")
            user = User.query.filter_by(email=user_email).first()
            if user:
                if user.password_hash == user_pass:
                    random_number = str(randint(0, 1000))
                    flash('successful login')  # falsh won't stay that long to copy
                    dashboard_keys.update({random_number: user.email})
                    return jsonify(
                        {
                            "token": random_number
                        }
                    )
                else:
                    flash('incorrect password')
                    return redirect(url_for('users.login'))
            else:
                flash('email is not registered')
                return redirect(url_for('users.register'))
    return render_template('login.html')


@user.route('/dashboard',methods=["POST"])
def dashboard():
    data = request.get_json()
    random = data.get("secret_key")
    if dashboard_keys.get(random):
            return render_template('dashboard.html')
    flash('You need to login first')
    return redirect(url_for('users.login'))


@user.route('/register')
def register():
    return render_template('register.html')


@user.route('/create', methods=["POST"])
def create():
    data = request.get_json()
    user = User(user_id=data.get("rollnumber"), name=data.get("name"), email=data.get("email"),
                password_hash=data.get("password"))
    db.session.add(user)
    db.session.commit()
    return 'success'
