x = int(input())
d = set()
for i in range(x):
    name, status = input().split()

    if status == "enter":
        d.add(name)
    elif status == "leave":
        d.remove(name)
for key in sorted(d, reverse = True):
    print(key)