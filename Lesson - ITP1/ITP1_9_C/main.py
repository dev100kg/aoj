n = int(input())
taro = 0
hanako = 0
for x in range(0, n):
    t, h = input().split()
    if t > h:
        taro += 3
    elif t < h:
        hanako += 3
    elif t == h:
        taro += 1
        hanako += 1
print(taro, hanako)
