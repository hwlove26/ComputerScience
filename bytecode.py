import dis

def task(x):
    while x != 26:
        x = x + 2
    return True

dis.dis(task)