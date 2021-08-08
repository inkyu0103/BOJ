# 17086 아기상어

from collections import deque
import sys
input = sys.stdin.readline

# 가장 가까운 거리의 상어와의 안전거리

def bfs(r,c):
    q = deque([(0,r,c)])
    visit = [[0]*M for _ in range(N)]
    visit[r][c] = 1

    while q:
        dist,r,c = q.popleft()

        if graph[r][c]:
            return dist

        for dr,dc in dirs:
            new_r,new_c = r+dr,c+dc
            if 0<=new_r<N and 0<=new_c <M and not visit[new_r][new_c]:
                visit[new_r][new_c] = 1
                q.append((dist+1,new_r,new_c))


if __name__=='__main__':
    N,M = map(int,input().split())
    graph = [list(map(int,input().split())) for _ in range(N)]
    dirs = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
    dist = 0

    for r in range(N):
        for c in range(M):
            if not graph[r][c]:
                dist = max(dist,bfs(r,c))

    print(dist)