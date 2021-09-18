# 17141 연구소 2
'''
0 빈칸
1 벽
2 바이러스 놓을 수 있는 칸
'''
import copy
from itertools import combinations
from collections import deque
import sys
input = sys.stdin.readline

def bfs(r,c):
    q = deque([[0,r,c]])
    visit[r][c] = 0

    while q :
        time,r,c = q.popleft()

        for dr,dc in dirs:
            new_r,new_c = r+dr,c+dc
            if 0<=new_r<N and 0<=new_c<N and graph[new_r][new_c] == 0 and visit[new_c][new_c] == -1:
                q.append([time+1,new_r,new_c])
                visit[new_r][new_c] = time+1






dirs = [(0,1),(0,-1),(1,0),(-1,0)]
N,M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
virus_candidate = []

# 바이러스를 놓을 수 있는 자리 찾기
for r in range(N):
    for c in range(N):
        if graph[r][c] == 2:
            virus_candidate.append([r,c])

for target in combinations(virus_candidate,M):
    visit = [[-1]*N for _ in range(N)]
    for r,c in target:
        bfs(r,c)
        for v in visit:
            print(v)
        break



