x = int(input())
y = int(input())

prime = []
for i in range(x, y+1):
    error = 0
    if i > 1 :
        for j in range(2, i):
            if i % j == 0:
                error += 1
                break
        if error == 0:
            prime.append(i)
            
if len(prime) > 0 :
    print(sum(prime))
    print(min(prime))
else:
    print(-1)
