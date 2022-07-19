from loginDAO.login_method import check


def check_log_in(u, p):
    # Lấy data từ file txt
    filename = "test.txt"
    user = []
    with open(filename) as f:
        for line in f:
            user.append([str(n) for n in line.strip().split(",")])
    
    return check(user, u, p)
