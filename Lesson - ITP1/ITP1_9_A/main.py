w = input()
cnt = 0
while True:
    t = input()
    if t == "END_OF_TEXT":
        break
    else:
        t = t.lower().split()
        cnt += t.count(w)
print(cnt)
