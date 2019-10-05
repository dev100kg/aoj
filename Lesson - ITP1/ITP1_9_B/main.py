while True:
    card = input()
    if card == "-":
        break
    else:
        m = int(input())
        for i in range(0, m):
            hi = int(input())
            card = card[hi:] + card[0:hi]
        print(card)
