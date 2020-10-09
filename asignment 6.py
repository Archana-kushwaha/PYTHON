min_length = 6
flag = True
name = input('please enter your name:')
while flag:
    name = input('please enter your name:')
    flag = not (name.isalpha() and name.isprintable() and len(name) >= min_length)

    print (f'name is {name}')