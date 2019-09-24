while True:
    xylist = []
    xylist = list(map(int, input().split()))
    if xylist[0] == xylist[1] == 0:
        break
    else:
        print(*sorted(xylist))
