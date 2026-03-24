x, y = map(int, input().split())
num = list(map(int, input().split()))

for i in range(x):
    if num[i] < y:
        print(num[i], end = " ")