squares = {
    0: lambda n: "#." * ((n // 2) + 1),
    1: lambda n: ".#" * ((n // 2) + 1), }
while True:
    h, w = map(int, input().split())
    if h == w == 0:
        break
    else:
        for x in range(h):
            print(squares[x % 2](w)[0:w])
        print()
