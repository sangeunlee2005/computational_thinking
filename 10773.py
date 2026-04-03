x = int(input())
z = []
for i in range(x):
    y = int(input())
    if y == 0:
        z.pop()
    else:
        z.append(y)
print(sum(z))