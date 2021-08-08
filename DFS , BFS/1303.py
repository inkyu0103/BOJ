# 1303 전투 - 첫 제출 인덱스 에러
from collections import deque
import sys
input = sys.stdin.readline


def bfs(target,r,c):
    q = deque([(r,c)])
    visit[r][c] = 1
    dist = 0
    while q:
        r,c = q.popleft()
        dist += 1
        for dr,dc in dirs:
            new_r,new_c = r+dr,c+dc

            if 0<=new_r<N and 0<=new_c<M and graph[new_r][new_c] == target and not visit[new_r][new_c]:
                visit[new_r][new_c] = 1
                q.append((new_r,new_c))

    return dist**2

M,N = map(int,input().split())
graph = [list(input().strip()) for _ in range(N)]

visit = [[0]*M for _ in range(N)]
dirs = [(0,1),(0,-1),(1,0),(-1,0)]
ally = 0
enemy = 0

for r in range(N):
    for c in range(M):
        if graph[r][c] and not visit[r][c]:
            if graph[r][c] == "W" and not visit[r][c]:
                ally += bfs("W",r,c)
            elif graph[r][c] == "B" and not visit[r][c]:
                enemy += bfs("B",r,c)

print(ally,enemy)



