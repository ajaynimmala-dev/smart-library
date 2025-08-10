from flask import render_template,Blueprint,request,redirect

from database.models import User, db

user = Blueprint('users',__name__)

@user.route('/login',methods=["POST","GET"])
def login():
    if request.method == "POST":
        if request.form:
            form = request.form
            user_email = form.get("email")
            user_pass = form.get("password")
            if User().is_user_valid(email=user_email,password=user_pass):
                return "success"
    return render_template('login.html')

@user.route('/register')
def register():
    return render_template('register.html')

@user.route('/create',methods=["POST"])
def create():
    data = request.get_json()
    user = User(user_id=data.get("rollnumber"),name=data.get("name"),email=data.get("email"),password_hash=data.get("password"))
    db.session.add(user)
    db.session.commit()
    return 'success'