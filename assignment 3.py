# working of  AND

num1 = 10
num2 = 12
num3 = 0

if num1 and num2 and num3:
    print("\nAll the numbers have boolean value as True\n")
else:
    print("\nAtleast one number has boolean value as False\n")

    # working of OR and  NOT
a = 10
if not a:
    print("Boolean value of a is True")

if not (a % 3 == 0 or a % 5 == 0):
    print("10 is not divisible by either 3 or 5\n")
else:
    print("10 is divisible by either 3 or 5\n")

