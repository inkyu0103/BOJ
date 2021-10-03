# 3372

import sys
input = sys.stdin.readline

def sol():
    N = int(input())
    graph = [list(map(int,input().split())) for _ in range(N)]
    dp = [[0]*N for _ in range(N)]


    dp[0][0] = 1


    for r in range(N):
        for c in range(N):
            if dp[r][c]:
                # 마지막은 셀 필요 x
                if r==N-1 and c==N-1:
                    continue

                if r + graph[r][c] < N:
                    if r+graph[r][c] == N-1 and c == N-1:
                        dp[r+graph[r][c]][c] += 1

                    else:
                        dp[r + graph[r][c]][c] = 1

                if c + graph[r][c] < N:
                    if r == N-1 and c+graph[r][c] == N-1:
                        dp[r][c+graph[r][c]] += 1

                    else:
                        dp[r][c+graph[r][c]] = 1

    print(dp[N-1][N-1])
sol()

'''
if dp[r][c] :
# 이렇게 하면 겹치는 경우가 생김 ex 3 2 1 1
if c+dp[r][c]<N:
dp[r][c+dp[r][c]] = graph[r][c+dp[r][c]]
if r+dp[r][c] < N:
dp[r+dp[r][c]][c] = graph[r+dp[r][c]][c]
'''