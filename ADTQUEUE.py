size = 8
numItem = 0
frontPointer = 0
backPointer = -1
queue = ["" for i in range(size)]

def Enqueue(Item : str):
    global numItem, backPointer
    if numItem >= size:
        print("full")
        return False
    backPointer += 1
    queue[backPointer] = Item
    numItem += 1
    return True

def Dequeue():
    global numItem, backPointer
    if numItem <= 0:
        print("empty")
        return False
    queue[frontPointer] = ""
    numItem -= 1
    for i in range(len(queue)-1):
        queue[i] = queue[i+1]
    backPointer -= 1

def ShowQueue():
    for i in range(len(queue)):
        print(queue[i])

while True:
    exec(input())