# 1743
from collections import deque
import sys
input = sys.stdin.readline

def bfs(r,c):
    q = deque([(r,c)])
    visit[r][c] = 1
    dist = 1

    while q:
        r,c = q.popleft()

        for dr,dc in dirs:
            new_r, new_c = r+dr,c+dc

            if 0<= new_r <N and 0<=new_c<M and graph[new_r][new_c] and not visit[new_r][new_c]:
                dist += 1
                q.append((new_r,new_c))
                visit[new_r][new_c] = 1

    return dist


N,M,K = map(int,input().split())
graph = [[0]*M for _ in range(N)]
visit = [[0]*M for _ in range(N)]
dirs = [(0,1),(0,-1),(1,0),(-1,0)]
answer = 0

for _ in range(K):
    r,c = map(int,input().split())
    graph[r-1][c-1] = 1


for r in range(N):
    for c in range(M):
        if graph[r][c] and not visit[r][c]:
            answer = max(answer,bfs(r,c))
print(answer)
