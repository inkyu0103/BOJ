# 2225
import sys
input = sys.stdin.readline

# 가로 숫자 / 세로 가짓수
def sol():
    N, K = map(int, input().split())

    dp = [[0] * (N+1) for _ in range(K+1)]

    # initialize : 1가지 방법으로 만드는 것은 1개 밖에 없음
    for n in range(N+1):
        dp[1][n] = 1

    for k in range(1, K+1):
        dp[k][0] = 1

    for k in range(2, K+1):
        for n in range(1, N+1):
            dp[k][n] = dp[k-1][n] + dp[k][n-1]

    print(dp[K][N] % 1000000000)
sol()