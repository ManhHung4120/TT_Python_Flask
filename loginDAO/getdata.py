
def get_data():
    # Lấy data từ file txt
    filename = "test.txt"
    user = []
    with open(filename) as f:
        for line in f:
            user.append([str(n) for n in line.strip().split(",")])
    
    return user
