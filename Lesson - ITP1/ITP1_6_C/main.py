n = int(input())

buildings = [[[0 for x in range(10)] for y in range(3)] for z in range(4)]

for x in range(n):
    b, f, r, v = map(int, input().split())
    buildings[b - 1][f - 1][r - 1] += v

for x in range(4):
    for floor in buildings[x]:
        print("", *floor)
    if x != 3:
        print("#" * 20)
