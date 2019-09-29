n, m = map(int, input().split())
arr_a = []
vec_b = []
for x in range(0, n):
    arr_a.append(list(map(int, input().split())))
for y in range(0, m):
    vec_b.append(int(input()))

for ni in range(0, n):
    s = 0
    for mi in range(0, m):
        s += (arr_a[ni][mi] * vec_b[mi])
    print(s)
