x = int(input())
y = int(input())

prime = []
for i in range(x, y+1):
    error = 0
    if i > 1 :
        for j in range(2, i):  # 2부터 num-1까지
            if i % j == 0:
                error += 1
                break  # 2부터 num-1까지 나눈 몫이 0이면 error가 증가하고 for문을 끝냄
        if error == 0:
            prime.append(i)  # error가 없으면 소수리스트에 추가
            
if len(prime) > 0 :
    print(sum(prime))
    print(min(prime))
else:
    print(-1)