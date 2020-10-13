def intersection(list1, list2):
    return list(set(list1) & set(list2))

list1 = [15, 9, 10, 56, 23, 78, 5, 4, 9]
list2 = [9, 4, 5, 36, 47, 26, 10, 45, 87]
print(intersection(list1, list2))