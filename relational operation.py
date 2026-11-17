num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
num4 = int(input("Enter fourth number: "))

if num1 > num2 :
    print("num 1 is greater than num 2 (TRUE)")
else:
    print("num 1 is not greater than num 2 (FALSE)")
if num3 < num4 :
    print("num 3 is less than num 4 (TRUE)")
else:
    print("num 3 is not less than num 4 (FALSE)")
if num1 == num3 :
    print("num 1 is equal to num 3 (TRUE)")
else:
    print("num 1 is not equal to num 3 (FALSE)")
if num2 >= num4 :
    print("num 2 is greater than or equals to num 4 (TRUE)")
else:
    print("num 2 is not greater than or equals to num 4 (FALSE)")
if num3 <= num1 :
    print("num 3 is less than or equal to num 1 (TRUE)")
else :
    print("num 3 is not less than num 1 (FALSE)")
if num1 != num4 :
    print("num 1 is not equal to num 4 (TRUE)")
else :
    print("num 1 is equal to num 4 (FALSE)")

if (num1 + num2) < (num3 - num4) :
    print("Sum of num1 and num2 is less than difference between num3 and num4")
else:
    print("Sum of num1 and num2 is not less than difference between num3 and num4")
if (num1 // num2) == (num3 * num4):
    print("Quotient obtained when num1 divided by num2 is equal to product of num3 and num4")
else:
    print("Quotient obtained when num1 divided by num2 is not equal to product of num3 and num4")

if (num1 - 5) >= 0 and (num2 - 10) >= 0:
    print("TRUE")
if (num3 + 10) <= 0 or (num4 + 3) <= 0:
    print("TRUE")

if num1 % 2 == 1:
    print("num1 is odd")