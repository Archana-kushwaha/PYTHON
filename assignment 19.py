Digit = int(input("Enter a number:"))
rev = 0

while ( Digit > 0 ) :
    a = Digit % 10
    rev = rev * 10 + a
    Digit = Digit // 10

print(rev)