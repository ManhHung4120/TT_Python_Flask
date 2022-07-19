from flask import Blueprint, render_template


login_bp = Blueprint("login_bp", __name__, template_folder="templates/login")


def success():
    return render_template("success.html")


def login():
    return render_template("login.html")


login_bp.add_url_rule("/success", view_func=success)
login_bp.add_url_rule("/login", view_func=login)
