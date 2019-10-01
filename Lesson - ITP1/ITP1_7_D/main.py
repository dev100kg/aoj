# TODO: 要見直し

n, m, l = map(int, input().split())
a = []
b = []
ans = []
for x in range(n):
    a.append(list(map(int, input().split())))
for y in range(m):
    b.append(list(map(int, input().split())))

# print(a, b)
sub_total = []
for e in range(0, n):
    tm2 = []
    for f in range(0, l):
        tmp = []
        for g in range(0, m):
            tmp.append(a[e][g] * b[g][f])
            if len(tmp) == m:
                tm2.append(sum(tmp))
                tmp.clear()
                if len(tm2) == l:
                    print(*tm2)
                    tm2.clear()
