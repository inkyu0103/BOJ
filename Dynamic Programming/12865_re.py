import sys
input = sys.stdin.readline

def sol():
    N,K = map(int,input().split())
    dp = [[0] * (N+1) for _ in range(K+1)]
    info = [[0,0]]

    for _ in range(N):
        info.append(list(map(int,input().split())))

    for k in range(1,K+1):
        for n in range(1,N+1):
            if k-info[n][0] >= 0:
                dp[k][n] = max(dp[k][n-1], dp[k-info[n][0]][n-1] + info[n][1])

            else:
                dp[k][n] = dp[k][n-1]

    print(dp[K][N])
sol()