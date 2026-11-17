my_list = [3,20,4,12,27,67,30,1]
swapped = False
n = len(my_list)


for i in range(len(my_list)):
    swapped = False
    for j in range(n-1):
        if my_list[j] > my_list[j+1]:
            temp = my_list[j]
            my_list[j] = my_list[j+1]
            my_list[j+1] = temp
            swapped = True
    if not swapped:
        break
    print(my_list)
    n -= 1
    print(n)


print("sorted list:" + str(my_list))


