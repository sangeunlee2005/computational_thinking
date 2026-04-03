y = []
for i in range(10):
    x = int(input())
    y.append(x % 42)
print(len(set(y)))