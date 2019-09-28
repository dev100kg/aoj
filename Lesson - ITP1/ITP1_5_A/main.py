while True:
    h, w = map(int, input().split())
    if h == w == 0:
        break
    else:
        for x in range(h):
            print("#" * w)
    print("")
