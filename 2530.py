a, b, c = map(int, input().split())
x = int(input()) 

c += x % 60
x = x // 60
if c >= 60:
    c -= 60
    b += 1

b += x % 60
x = x // 60
if b >= 60:
    b -= 60
    a += 1

a += x % 24
if a >= 24:
    a -= 24

print(a, b, c)