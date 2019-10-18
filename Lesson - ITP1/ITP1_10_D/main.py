n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

distance = {
    1: lambda: sum([abs(x[i] - y[i]) for i in range(n)]),
    2: lambda: pow(sum([pow(abs(x[j] - y[j]), 2) for j in range(n)]), 1 / 2),
    3: lambda: pow(sum([pow(abs(x[j] - y[j]), 3) for j in range(n)]), 1 / 3),
    4: lambda: max([abs(x[i] - y[i]) for i in range(n)])
}

print(distance[1]())
print(distance[2]())
print(distance[3]())
print(distance[4]())
