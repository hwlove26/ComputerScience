
topPointer = -1
size = 8
stack = ["" for i in range(size)]

def Push(newData : str):
    global topPointer
    print(size)
    if topPointer + 1 >= size:
        print("alr full")
    else:
        topPointer = topPointer + 1
        stack[topPointer] = newData

def Pop():
    global topPointer
    if topPointer - 1 < -1:
        print("alr empty")
    else:
        stack[topPointer] = ""
        topPointer = topPointer - 1


def Show():
    for i in range(size - 1, -1, -1):
        print(stack[i])

while True:
    exec(input())