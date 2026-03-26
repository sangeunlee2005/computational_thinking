x, y = map(int, input().split())
z = int(input())
y += z
if y >= 60:
    x = x + y // 60
    y = y % 60
if x >= 24:
    y = y % 60
    x -= 24
print(x, y)