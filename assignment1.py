num = 100
if num < 0:
   print("Enter a positive number")
else:
   sum = 0
   while(num > 0):
       sum += num
       num -= 1
n = 0
for i in range(1,100):
      if not i % 13 or  not i % 7 or  not i % 3:
              n=n+i
print(sum-n)