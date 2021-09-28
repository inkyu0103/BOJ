# 1446 지름길
import sys
input = sys.stdin.readline

def sol():
    N, D = map(int, input().split())
    path = [list(map(int, input().split())) for _ in range(N)]
    dis = [i for i in range(D+1)]
    for i in range(D+1):
        if i > 0:
            dis[i] = min(dis[i], dis[i-1]+1)
        for s, e, d in path:
            if i == s and e <= D and dis[i]+d < dis[e]:
                dis[e] = dis[i]+d
    print(dis[D])
sol()
