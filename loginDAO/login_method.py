from loginDAO.getdata import get_data
# Xử lý logic check tài khoản
def check(u,p):
    user = get_data()
    for pair in user:
        username, password = pair[0], pair[1]
        if u == username and p == password:
            return True
