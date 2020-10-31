def check_anagram(s1, s2):
    if sorted(s1) == sorted(s2):
        print("True.")
    else:
        print("False")


s1 = input("Enter first string:")
s2 = input("Enter second string:")
check_anagram(s1, s2)
