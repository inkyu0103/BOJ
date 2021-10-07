# 14502_1
from collections import deque
from itertools import combinations
import copy
import sys
input = sys.stdin.readline

def sol():
    def bfs():

        visit = [[0]*C for _ in range(R)]
        q = deque()

        for virus in viruses:
            r,c = divmod(virus,C)
            q.append([r,c])
            visit[r][c] = 1
            wall_map[r][c] = 2


        while q:
            r,c = q.popleft()

            for dr,dc in dirs:
                if 0<=r+dr<R and 0<=c+dc<C and not visit[r+dr][c+dc] and wall_map[r+dr][c+dc] == 0:
                    q.append([r+dr,c+dc])
                    visit[r+dr][c+dc] = 1
                    wall_map[r+dr][c+dc] = 2



        result = 0

        for r in range(R):
            for c in range(C):
                if not wall_map[r][c]:
                    result += 1

        return result


    R,C = map(int,input().split())
    _map = [list(map(int,input().split())) for _ in range(R)]
    dirs = [(0,1),(0,-1),(1,0),(-1,0)]
    viruses = set()
    # 0. 바이러스가 있는 칸에 대해서 정보를 저장해 놓는다. set으로 해놓든 뭘로 하던...
    for r in range(R):
        for c in range(C):
            if _map[r][c] == 2:
                viruses.add(r*C +c)

    # 1. 조합을 통해 벽을 세워놓을 위치를 정한다. : 바이러스와 기존 벽이 아닌 곳을 추가.
    walls = []

    for r in range(R):
        for c in range(C):
            if _map[r][c] == 0:
                walls.append(r*C+c)

    result = 0

    for targets in combinations(walls,3):
        wall_map = copy.deepcopy(_map)
        for target in targets:
            r,c = divmod(target,C)
            wall_map[r][c] = 1

        count = bfs()
        result = max(result,count)

    print(result)

sol()