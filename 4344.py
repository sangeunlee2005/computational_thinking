x = int(input())
for i in range(x):
    y = list(map(int, input().split()))
    a = y[0]
    b = y[1:]
    c = 0
    for j in b:
        if j > (sum(b)/a):
            c += 1
    d = (c / a) * 100
    print(f"{d:.3f}%")