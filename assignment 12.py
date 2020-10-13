original_list = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]

flatten_list = []


def reemovNestings(original_list):
    for i in original_list:
        if type(i) == list:
            reemovNestings(i)
        else:
            flatten_list.append(i)


print('The original list: ', original_list)
reemovNestings(original_list)
print('The list after removing nesting: ', flatten_list)