x = int(input())
y = list(map(int, input().split()))
z = 0
for i in range(x):
    for j in range(i + 1, x):
        z += abs(y[i] - y[j])
print(z * 2)            #Python 3으로는 시간초과