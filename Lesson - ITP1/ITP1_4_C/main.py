while True:
    list_input = input().split()
    calculate = {'+': lambda a, b: a + b,
                 '-': lambda a, b: a - b,
                 '/': lambda a, b: a // b,
                 '*': lambda a, b: a * b,
                 }
    if list_input[1] == '?':
        break
    else:
        print(calculate[list_input[1]](int(list_input[0]), int(list_input[2])))
