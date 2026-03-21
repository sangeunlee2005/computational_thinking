x, y = map(str, input().split())
x = int(x, 2)
y = int(y, 2)
z = x + y
print(bin(z)[2:])