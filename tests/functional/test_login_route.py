from flask import url_for, request

DATA = [
    {"username": "hung", "password": "12314", "expect": "/login"},
    {"username": "abcd", "password": "1024", "expect": "/success"},
]


def test_login_wrong_username_password(client):

    with client:

        res = client.post("/login", data=DATA[0], follow_redirects=True)
        assert res.status_code == 200
        assert res.request.path == DATA[0].get("expect")


def test_login_username_password(client):

    with client:

        res = client.post("/login", data=DATA[1], follow_redirects=True)
        assert res.status_code == 200
        assert res.request.path == DATA[1].get("expect")
