# 11049 행렬 곱셈 순서
'''
행렬 A*B*C 가 있다면

A*(B*C)나 (A*B)*C나 결과는 같으나 계산 횟수가 다르다는 점이 있다.

n개의 행렬이 주어질 때,

1개~연속 n개(최대 행렬 개수)

ex)
사실 처음 시도에는 의미 x
1개~ N개(최대 행렬 개수)
A*B*C*D*E*F*G
(A*B)*C*D*E*F*G

A부터, B부터...N부터...
ex)
A*(B*C)*D*E*F*G
A*(B*C*D)*E*F*G 라고 하면

(B*C*D) 내부에서도 어느 방법이 가장 작은지 알아야 한다.

몇개 연속 ? (2개 ~ n-1개)

'''


def solve(arr):
    # 행렬의 개수
    num_mat = len(arr) - 1

    # dyn 초기화
    dyn = [[0] * num_mat for i in range(num_mat)]

    # 연속으로 곱할 matrix의 개수 (2~ 행렬 개수)
    for cl in range(2, num_mat):
        # i 는 시작 행렬, j는 끝 행렬 (cl만큼 차이)
        # ABCDEF 기준 4번 행렬이 끝 따라서 num_mat-cl은 5가 나와야함
        # arr a a b c e d f
        for i in range(1, num_mat-cl+2):
            j = i + cl
            dyn[i-1][j-1] = MAX
            # chain 사이에 있는 것들
            for k in range(i, j):
                q = dyn[i-1][k-1] + dyn[k][j-1] + arr[i-1] * arr[k-1] * arr[j-1]
                if q < dyn[i-1][j-1]:
                    dyn[i-1][j-1] = q
    return dyn

import sys
MAX = 1e20
box = []

case = int(input())
for i in range(case):
    s,e = map(int,sys.stdin.readline().split())
    if i == 0:
        box.append(s)
        box.append(e)
    else:
        box.append(e)


print(solve(box))





