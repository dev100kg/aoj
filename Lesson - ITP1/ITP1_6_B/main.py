card_list = [y + " " + str(x) for y in ("SHCD") for x in range(1, 14)]

n = int(input())
if n != 52:
    for y in range(n):
        card_list.remove(input())
    print(*card_list, sep='\n')
