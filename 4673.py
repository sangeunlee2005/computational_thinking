x = set()
y = set()
for i in range(1, 10001):
    x.add(i)
for i in range(1, 10001):
    if i >= 1000:
        y.add(i + (i // 1000) + ((i // 100) % 10) + ((i // 10) % 10) + (i % 10))
    elif i >= 100:
        y.add(i + (i // 100) + ((i // 10) % 10) + (i % 10))
    else:
        y.add(i + (i // 10) + (i % 10))
z = sorted(x - y)
for i in range(len(z)):
    print(z[i])