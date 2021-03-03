# 2740 행렬곱셈

import sys

def sol():
    N,M = map(int,sys.stdin.readline().split())
    matrix1 = [[int(i) for i in sys.stdin.readline().split()]  for _ in  range(N)]
    M,K = map(int,sys.stdin.readline().split())
    matrix2 = [[int(i) for i in sys.stdin.readline().split()]  for _ in  range(M)]

    matrix3 = [[0]*K for _ in range(N)]


    for n in range(N):
        for k in range(K):
            result = 0
            for m in range(M):
                result += matrix1[n][m]*matrix2[m][k]

            matrix3[n][k] = result




    for n in range(N):
        for k in range(K):
            print(matrix3[n][k],end=" ")
        print()



sol()
