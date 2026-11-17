my_list = [3,1,2,5,0]
found = False
target = 3

for i in range(len(my_list)):
    if my_list[i] == target:
        found = True
        break

if found:
    print("found")
else:
    print("not found")