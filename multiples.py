def multiplesOf3Or5(maxNum: int) :
    maxNum = maxNum - 1 #minus 1 to exclude the number of parameter
    num5= maxNum // 5 #to get number of multiples of 5
    num3 = maxNum // 3 #to get number of multiples of 3
    sum = 0
    for i in range(1, num5 + 1) :
        sum = sum + 5*i
    for i in range(1, num3 + 1):
        sum = sum + 3*i
    return sum

x = int(input()) # input limit
print(multiplesOf3Or5(x))