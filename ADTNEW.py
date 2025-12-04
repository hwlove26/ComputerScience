StackList = []
Top = -1

def PushItem():
    global Top
    newValue = input("enter a value to add")
    Top = Top + 1
    StackList[Top] = newValue

def PopItem():
    global Top
    if Top - 1 < -1:
        print("Stack Underflow")
    else:
        StackList[Top] = ""
        Top = Top - 1

def DisplayStack():
    for i in range (Top - 1, -1, -1):
        print(StackList[i])

while True:
    choice = input()
    match choice:
        case "Push":
            PushItem()
        case "Pop":
            PopItem()
        case "Display":
            DisplayStack()
        case "Quit":
            break
        case _:
            print("try again")