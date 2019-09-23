W, H, x, y, r = map(int, input().split())
rx1 = x + r
rx2 = x - r
ry1 = y + r
ry2 = y - r

if rx1 <= W and rx1 >= 0:
    if rx2 <= W and rx2 >= 0:
        if ry1 <= H and ry1 >= 0:
            if ry2 <= H and ry2 >= 0:
                print("Yes")
                exit()
print("No")
