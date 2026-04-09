x = int(input())
y = {}
for i in range(x):
    z = input()
    if z in y:
        y[z] += 1
    else:
        y[z] = 1
a = max(y.values())
b = []
for i in y:
    if y[i] == a:
        b.append(i)
b = sorted(b)
print(b[0])