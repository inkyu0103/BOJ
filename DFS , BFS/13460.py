# 13460 구슬 탈출 2
import sys
input = sys.stdin.readline
from collections import deque

'''
상자를 이리저리 흔들어서 하는건데, 동시에 움직이는건 말이 안되고 하나씩 해봐야 하나

- 파란 구슬이 구멍에 빠지면 실패
- 동시에 구슬이 빠져도 실패
# 는 장애물, O는 구멍의 위치 R / B 는 각각 구슬의 색깔

조건을 조금 다르게 해야하네.
이전 방향과 같은 방향으로 움직이면 카운트에 추가를 하지 않는 방향

'''


def find_RBO(N,M):
    R = (-1,-1)
    B = (-1,-1)
    O = (-1,-1)

    for r in range(N):
        for c in range(M):
            if graph[r][c] == "R":
                R = (r,c)
            elif graph[r][c] =="B" :
                B = (r,c)
            elif graph[r][c] == "O" :
                O = (r,c)

    return R,B,O

def BFS(start,N,M,O):
    visit = [[0]*M for _ in range(N)]
    q = deque([start])

    length = 1
    count = 0
    dist = 1

    while q:
        cur_r,cur_c = q.popleft()
        visit[cur_r][cur_c] = 1

        count += 1

        for move in dirs:
            move_r , move_c = move
            new_r,new_c = cur_r+move_r , cur_c+move_c

            if (new_r,new_c) == O:
                print(visit)
                return dist

            if 0<new_r<N and 0<new_c<M and graph[new_r][new_c] =="." and not visit[new_r][new_c]:
                q.append((new_r,new_c))

        if count == length:
            length = len(q)
            count = 0
            dist += 1

    return -1


if __name__=='__main__':
    N,M = map(int,input().split())
    graph=[list(input().strip()) for _ in range(N)]
    dirs = [(0,1),(0,-1),(1,0),(-1,0)]
    R,B,O = find_RBO(N,M)
    print(R,B,O)

    print(BFS(R,N,M,O))
