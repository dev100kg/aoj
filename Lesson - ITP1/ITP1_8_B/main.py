while True:
    x = input()
    if int(x) == 0:
        break
    else:
        sum = 0
        for i in x:
            sum += int(i)
    print(sum)
