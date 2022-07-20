from flask import render_template, request, redirect, url_for, jsonify
from loginDAO.login_method import check


def passdata(body):
    username = body["username"]
    password = body["password"]
    return check(username, password)
