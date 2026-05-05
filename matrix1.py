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

def calc(A, B, C, n):
    result = []

    for i in range(n):
        row = []
        for j in range(n):
            val = 0
            for k in range(n):
                val += A[i][k] * B[k][j]
            val += C[i][j]
            row.append(val)
        result.append(row)
    return result

n = int(input())

A, B, C = gen(n), gen(n), gen(n)

print("A: ")
pr(A)
print("B: ")
pr(B)
print("C: ")
pr(C)

print("A x B + C: ")
pr(calc(A, B, C, n))