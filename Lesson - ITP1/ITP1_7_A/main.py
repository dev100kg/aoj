while True:
    result = ""
    m, r, f = map(int, input().split())
    if m == r == f == -1:
        break
    judgement = m + r
    if m == -1 or r == -1:
        result = "F"
    elif judgement >= 80:
        result = "A"
    elif judgement >= 65 and judgement < 80:
        result = "B"
    elif judgement >= 50 and judgement < 65:
        result = "C"
    elif judgement >= 30 and judgement < 50:
        if f >= 50:
            result = "C"
        else:
            result = "D"
    elif judgement < 30:
        result = "F"
    print(result)
