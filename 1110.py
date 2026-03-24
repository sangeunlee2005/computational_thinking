n = int(input())
num = n
a = 0

while True:
    x = n // 10
    y = n % 10
    z = (x + y) % 10
    n = (y * 10) + z

    a += 1
    if n == num:
        break
print(a)