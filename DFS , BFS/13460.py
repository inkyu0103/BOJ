# 13460 구슬탈출 2  / 시작 9시 / 1차 시도(30분) - 생각만 함. / 답보고 이해 (30분)
# 재도전 8월 2일 9시 시작 : 9시 반 시간초과

from collections import deque
import sys
input = sys.stdin.readline

def bfs(R,B,O):
    red_q = deque([R])
    blue_q = deque([B])

    red_visit =[[0]*C for _ in range(R)]
    blue_visit=[[0]*C for _ in range(R)]

    red_visit[R[0]][R[1]] = 1
    blue_visit[B[0]][B[1]] = 1


    while red_q or blue_q:
        rr,rc = red_q.popleft()
        br,bc = blue_q.popleft()

        for dr,dc in dirs:


            while 0<=rr+dr<R and 0<=rc+dc<C and not graph[rr+dr][rc+dc]==".":
                rr += dr
                rc += dc

            while 0<=br+dr<R and 0<=bc+dc<C and graph[br+dr][bc+dc] ==".":
                br += dr
                bc += dc










def find_location():
    R,B,O = (-1,-1),(-1,-1),(-1,-1)
    for r in range(R):
        for c in range(C):
            if graph[r][c] == "R":
                R = (r,c)
            elif graph[r][c] =="B":
                B = (r,c)
            elif graph[r][c] =="O":
                O = (r,c)

    return R,B,O

if __name__ =='__main__':
    R,C = map(int,input().split())
    graph = [list(input().strip()) for _ in range(R)]
    dirs = [(0,1),(0,-1),(1,0),(-1,0)]
    R,B,O = find_location()



