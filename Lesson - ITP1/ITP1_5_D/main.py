n = int(input())
tmp = ''
for x in range(3, n + 1):
    if x % 3 == 0 or str(x).find('3') >= 0:
        tmp += ' ' + str(x)
print(tmp)
