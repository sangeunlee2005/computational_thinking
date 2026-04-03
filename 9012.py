x = int(input())
for _ in range(x):
    s = input()
    a = 0
    valid = True
    for ch in s:
        if ch == "(":
            a += 1
        else:
            a -= 1
        if a < 0:
            valid = False
            break
    if a == 0 and valid:
        print("YES")
    else:
        print("NO")