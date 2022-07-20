from flask import Blueprint, make_response, render_template, request,jsonify
from login.route import passdata
login_bp = Blueprint("login_bp", __name__, template_folder="templates/login")


@login_bp.route("/login", methods=["POST"])
def check_login():
    body = request.get_json()
    if passdata(body) == True :
        return make_response(jsonify(Status =  "Đăng nhập thành công"))
    else :
        return make_response(jsonify(Status = "Đăng nhập thất bại"))
    