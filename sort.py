a = [8, 4, 9, 5]
tmp = 0
for i in range(len(a)):
    for j in range(len(a) - 1):
        if a[j] > a[j+1]:
            tmp = a[j]
            a[j] = a[j+1]
            a[j+1] = tmp
print(a)