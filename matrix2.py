import random

def gen(n):
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(random.randint(1, n*n*10-1))
        matrix.append(row)
    return matrix

def pr(m):
    for r in m:
        for i in r:
            print(f"{i:4}", end=" ")
        print()

def trans(m):
    result = [[0]*n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            result[j][i] = m[i][j]
    return result

n = int(input())

A = gen(n)

print("A: ")
pr(A)

print("전치행렬: ")
pr(trans(A))