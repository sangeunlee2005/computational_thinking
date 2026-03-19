x = 0
y = []

for i in range(4):
    a, b = map(int, input().split())
    x = x - a
    x = x + b
    y.append(x)
print(max(y))
print(y)