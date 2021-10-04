# 3197 BFS 최적화
from collections import deque
import sys
input = sys.stdin.readline

def sol():
    R,C = map(int,input().split())
    _map = [list(input().rstrip().split()) for _ in range(R)]
    _visit = [[0]*C for _ in range(R)]

    swan = [-1,-1]
    dirs = [[0,1],[0,-1],[1,0],[-1,0]]
    for r in range(R):
        for c in range(C):
            if _map[r][c] == "L":
                swan = [r,c]

    q_ice = deque()

    q_swan = deque()
    q_swan.append(swan)
    _visit[swan[0]][swan[1]] = 1


    def bfs_swan():
        tmp_q = deque()

        while q_swan:
            r,c=q_swan.popleft()

            for dr,dc in dirs:
                if 0<= r+dr < R and 0<=c+dc< C and not _visit[r+dr][c+dc]:


















sol()