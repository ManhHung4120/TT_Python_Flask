from flask import render_template, request, redirect, url_for, jsonify
from login.blueprint import login_bp
from loginDAO.getdata import check_log_in


@login_bp.route("/login", methods=["POST"])
def check_login():

    username = request.form["username"]
    password = request.form["password"]

    if check_log_in(username, password) == True:
        return redirect("/success")

    else:
        return redirect("/login")
