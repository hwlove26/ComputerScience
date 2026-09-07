from random import  randint

print("Rock, Paper, Scissors!")
choice = input("Enter your choice: 1 for rock, 2 for paper, 3 for scissors\n")
cpuchoice = randint(1,3)
if cpuchoice == 1:
    print("Rock!")
    if choice == "1":
        print("tie")
    elif choice == "2":
        print("win")
    elif choice == "3":
        print("lose")
elif cpuchoice == 2:
    print("Paper!")
    if choice == "1":
        print("lose")
    if choice == "2":
        print("tie")
    if choice == "3":
        print("win")
elif cpuchoice == 3:
    print("Scissors!")
    if choice == "1":
        print("win")
    if choice == "2":
        print("lose")
    if choice == "3":
        print("tie")
if not choice == "1" and not choice == "2" and not choice == "3":
    print("Invalid input")