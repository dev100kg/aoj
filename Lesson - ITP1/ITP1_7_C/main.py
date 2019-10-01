r, c = map(int, input().split())
sums = [0] * (c + 1)
for x in range(0, r):
    raw = list(map(int, input().split()))
    raw_t = 0
    for x in range(0, c):
        sums[x] += raw[x]
        raw_t += raw[x]
    raw.append(raw_t)
    sums[c] += raw_t
    print(*raw)
print(*sums)
