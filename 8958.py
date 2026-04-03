x = int(input())
y = 0
a = 0
for i in range(x):
    z = list(input())
    for j in range(len(z)):
        if z[j] == "O":
            y += 1
            a += y
        elif z[j] == "X":
            y = 0
    y = 0
    print(a)
    a = 0