def perfect_number(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n
n = int(input("Enter a number:"))
if(perfect_number(n)):
    print(n,"is a perfect number")
else:
    print(n,"is not a perfect number")

