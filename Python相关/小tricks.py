# 简化多if分支
def print_status(status):
    if status == '0':
        print(0)
    elif status == '1':
        print(1)
    elif status == '2':
        print(2)
    elif status == '3':
        print(3)

def print_status(status):
    status_dict = {
        '0':0,
        '1':1,
        '2':2,
        '3':3
    }

    print(status_dict.get(status))