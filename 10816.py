n = int(input())
x = list(map(int, input().split()))

m = int(input())
y = list(map(int, input().split()))

cnt = {}

for i in x:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

for i in y:
    print(cnt.get(i, 0), end=" ")