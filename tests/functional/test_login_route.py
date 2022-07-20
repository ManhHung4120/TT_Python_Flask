from flask import url_for, request, json
import json


DATA = [
    {"username": "hung", "password": "12314", "expect": {"Status": "False"}},
    {"username": "abcd", "password": "1024", "expect": {"Status": "Success"}},
]


def test_login_wrong_username_password(app, client):
    # del app
    with client:

        response = client.post("/login", json=DATA[0])
        res = json.loads(response.get_data(as_text=True))
        assert response.status_code == 200
        assert res == DATA[0].get("expect")


def test_login_username_password(client):
    # del app
    with client:

        response = client.post("/login", json=DATA[1])
        res = json.loads(response.get_data(as_text=True))
        assert response.status_code == 200
        assert res == DATA[1].get("expect")
