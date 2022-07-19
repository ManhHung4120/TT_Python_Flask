# Xử lý logic check tài khoản
def check(user, u, p):
    for pair in user:
        username, password = pair[0], pair[1]
        if u == username and p == password:
            return True
