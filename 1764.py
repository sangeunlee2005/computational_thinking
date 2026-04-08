x, y = map(int, input().split())
a = set()
b = set()
for i in range(x):
    a.add(input())
for i in range(y):
    b.add(input())
c = sorted(list(a&b))
print(len(c))
for i in c:
    print(i)