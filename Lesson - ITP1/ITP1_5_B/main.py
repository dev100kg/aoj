while True:
    h, w = map(int, input().split())
    if h == w == 0:
        break
    else:
        for x in range(h):
            if x == 0 or x == h - 1:
                print("#" * w)
            else:
                str = ""
                for y in range(w):
                    if y == 0 or y == w - 1:
                        str += "#"
                    else:
                        str += "."
                print(str)
        print("")
