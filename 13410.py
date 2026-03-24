x, y  = map(int, input().split())
n = []

for i in range(1, y+1):
    n.append(int(str(x*i)[::-1]))

print(max(n))