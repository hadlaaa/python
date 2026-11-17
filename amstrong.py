def check(n):
    s = 0
    for i in str(n):
        s += int(i) ** len(str(n))
    return s == n
