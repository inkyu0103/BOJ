# 11444 피보나치 수 6
import sys

input = sys.stdin.readline


def mul_matrix(mat1, mat2):
    result = [[0] * 2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += mat1[i][k] * mat2[k][j] % 1000000007
    return result


def pow(mat, n):
    if n == 1:
        return mat

    tmp = pow(mat, n // 2)
    if n % 2:
        return mul_matrix(mul_matrix(tmp, tmp), mat)

    return mul_matrix(tmp, tmp)


def sol():
    N = int(input())
    matrix = [[1, 1], [1, 0]]

    answer = pow(matrix, N)
    print(answer[0][1] % 1000000007)


sol()
