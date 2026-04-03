x = int(input())
y = []
for i in range(x):
    z = int(input())
    y.append(z)
y.sort()
for i in range(x):
    print(y[i])