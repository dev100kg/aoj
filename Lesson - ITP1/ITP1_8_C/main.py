ans = {chr(i): 0 for i in range(97, 97 + 26)}
while True:
    try:
        s = input()
    except BaseException:
        break
    s = s.lower()
    for si in s:
        if si.isalpha():
            ans[si] += 1

for x, y in ans.items():
    print(x, ':', y)
