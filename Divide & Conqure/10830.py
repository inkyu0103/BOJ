# 10830 행렬제곱
import sys

input = sys.stdin.readline


def mul_matrix(mat1, mat2):
    N = len(mat1)
    result = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += mat1[i][k] * mat2[k][j] % 1000
    return result


def power(mat, n):
    if n == 1:
        return mat

    half = power(mat, n // 2)

    if n % 2:
        return mul_matrix(mul_matrix(half, half), mat)
    else:
        return mul_matrix(half, half)


def sol():
    N, B = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(N)]

    result = power(mat, B)

    for i in result:
        print(*list(map(lambda x: x % 1000, i)))


sol()
