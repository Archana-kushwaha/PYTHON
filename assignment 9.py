list_1 = [11, 7, 15, 60, 31, 8]

value = 10

print("The list : " + str(list_1))

count = len([i for i in list_1 if i > value])

print("The number of elements greater than 10 : " + str(count))