myArray = []
for i in range(0,7):
    myArray.append(int(input()))
myArray.sort()

print("enter target")
target = int(input())
start = 0
end = len(myArray)-1
found = False
while found == False:
    mid = int((start + end) / 2)
    print(mid)
    if myArray[mid] == target:
        found = True
        print("found at", mid)
    elif start > end:
        print("cannot find")
        break
    elif myArray[mid] < target:
        start = mid + 1
    elif myArray[mid] > target:
        end = mid - 1
    print(mid)