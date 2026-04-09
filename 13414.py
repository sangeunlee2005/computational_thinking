import sys
input = sys.stdin.readline

x, y = map(int, input().split())
table = dict()

for _ in range(y):
    z = input().rstrip()
    if z in table:
        table.pop(z)
    table[z] = 1

for key in list(table.keys())[:x]:
    print(key)