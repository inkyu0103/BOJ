# 3197 백조의 호수
from collections import deque
import sys
input = sys.stdin.readline

def find_swan_loc(lake,R,C):
    for r in range(R):
        for c in range(C):
            if lake[r][c] == 'L':
                return [r,c]

def sol():
    dirs=[[0,1],[0,-1],[1,0],[-1,0]]
    R,C = map(int,input().split())
    lake = [list(input().strip()) for _ in range(R)]
    swan_loc = find_swan_loc(lake,R,C)
    day = 0


    def swan_can_meet():
        visit = [[0]*C for _ in range(R)]
        q = deque([swan_loc])
        r,c = swan_loc
        visit[r][c] = 1

        while q:
            cur_r,cur_c = q.popleft()

            for dr,dc in dirs:
                new_r,new_c = cur_r+dr,cur_c+dc

                if 0<=new_r<R and 0<=new_c<C and not visit[new_r][new_c]:
                    if lake[new_r][new_c] == '.':
                        q.append([new_r,new_c])
                        visit[new_r][new_c] = 1

                    if lake[new_r][new_c] == 'L':
                        return True
        return False

    # 처음에 녹을 얼음 찾기
    def initial_melted_ice():
        melted_ice = []

        for r in range(R):
            for c in range(C):
                if lake[r][c] == 'X':
                    for dr, dc in dirs:
                        new_r,new_c = r+dr,c+dc

                        if 0<=new_r<R and 0<=new_c<C and lake[new_r][new_c] == '.':
                            melted_ice.append([r,c])

        return melted_ice

    def find_melted_ice(before_melted_ice):
        next_melted_ice = []











sol()