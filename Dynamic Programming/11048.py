# 11048
import sys
input = sys.stdin.readline

def sol():
    N,M = map(int,input().split())
    _map = [list(map(int,input().split())) for _ in range(N)]
    dirs = [(0,1),(0,-1),(1,0),(-1,0)]
    dp = [[0]*M for _ in range(N)]
    dp[0][0] = _map[0][0]

    for r in range(N):
        for c in range(M):
            for dr,dc in dirs:
                new_r,new_c = r+dr,c+dc
                if 0<= new_r < N and 0<= new_c < M:
                    dp[new_r][new_c] = max(dp[new_r][new_c], dp[r][c] + _map[new_r][new_c])

    print(dp[N-1][M-1])
sol()