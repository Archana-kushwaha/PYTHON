i=0
a=int(input())
n=0
while i <= a:
    user_input=(input('Enter the input:\n'))
    if user_input!='q':
        n=n+int(user_input)
        print('Enter to continue or q to quit')
        i=i+1
    else:
        print('You have chosen to quit')
        break
avg=n/i
print("total time the user entered the value is : %d " %i)
print("Average : %d" %avg)


