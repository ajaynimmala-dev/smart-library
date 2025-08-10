from flask import Blueprint,request

auth = Blueprint("auth", __name__)


@auth.route("/login",methods=["POST","GET"])
def auth_login():
    return "success"
