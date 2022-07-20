from flask import url_for, request, json
import json



DATA = [
    {"username": "hung", "password": 12314},
    {"username": "abcd", "password": 1024}
]


def test_login_wrong_username_password(app,client):
    del app
    # with client:

    response = client.post("/login", data= json.dumps(DATA[0]))
        # res = json.loads(response.get_data(as_text=True))
        # expect = {"Status" : "False"}
    assert response.status_code == 200
        # assert res == json.dumps(expect)
        


def test_login_username_password(app,client):
    del app
    # with client:

    response = client.post("/login", data=json.dumps(DATA[1]))
        # res = json.loads(response.get_data(as_text=True))
        # expect = {"Status" : "Success"}
    assert response.status_code == 200
        # assert res == json.dumps(expect)
