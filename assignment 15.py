def isPalindrome(My_str):
    for i in range(0, int(len(My_str) / 2)):
        if My_str[i] != My_str[len(My_str) - i - 1]:
            return False
    return True


s = input("Enter string:")
ans = isPalindrome(s)

if (ans):
    print(s,"is palindrome")
else:
    print(s,"is not palindrome")