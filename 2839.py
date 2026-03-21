x = int(input())
count = 0
while x >= 0:
    if x % 5 == 0:
        count += x // 5
        print(count)
        break
    x -= 3
    count += 1
else:
    print(-1)