#15489 파스칼의 삼각형
import sys
input = sys.stdin.readline


def sol():
    # 1. 삼각형을 만들자.
    R,C,W = map(int,input().split())
    tri = [[0]*30 for _ in range(30)]
    for i in range(30):
        tri[i][i] = 1
        tri[i][0] = 1

    for i in range(30):
        for j in range(i):
            if not tri[i][j]:
                tri[i][j] = tri[i-1][j-1]+tri[i-1][j]
    result = 0

    for i in range(W):
        for j in range(i+1):
            result += tri[R-1+i][C-1+j]
    print(result)


sol()
