while True:
    n, x = map(int, input().split())
    cnt = 0
    if n == x == 0:
        break
    if x >= 6:
        for a in range(1, n - 1):
            for b in range(a + 1, n):
                for c in range(b + 1, n + 1):
                    if a + b + c == x:
                        cnt += 1
    print(cnt)
