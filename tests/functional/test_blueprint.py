import pytest
from unittest import mock
from unittest.mock import patch

DATA = [
    (1,{"username": "hung", "password": "12314"}, {"Status": "False"},200),
    (2,{"username": "abcd", "password": "1024"},{"Status": "Success"},200),
]

@pytest.mark.parametrize('case, data, return_value,expect', DATA)
def test_adminfulfillingcount(case, data, return_value, expect,client):
    
    mock.patch('login.blueprint.check_login', return_value=return_value).start()
   
    response = client.post('/login', json = data, content_type='application/json')
    assert expect == response.status_code
    
    