import math
while True:
    n = int(input())
    if n == 0:
        break
    else:
        arr_s = list(map(int, input().split()))
        m = sum(arr_s) / n
        t = 0
        for si in arr_s:
            t += (si - m) ** 2
        print(math.sqrt(t / n))
