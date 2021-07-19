# 1388 바닥 장식
import sys
from collections import deque
input = sys.stdin.readline

'''
새로운 방문지를 찾아야 하는 find_not_visit
bfs를 
'''

def find_not_visit (N,M):
    for r in range(N):
        for c in range(M):
            if not visit[r][c]:
                return (r,c)
    return -1

def bfs(N,M,r,c):
    q = deque([(r,c)])

    while q:
        r,c = q.popleft()
        visit[r][c] = 1

        shape = graph[r][c]

        if shape == '-':
            for move in LR:
                m_r , m_c =move
                new_r, new_c = r+m_r , c+m_c

                if 0<=new_r<N and 0<=new_c<M and shape == graph[new_r][new_c] and not visit[new_r][new_c]:
                    q.append((new_r,new_c))


        elif shape == '|':
            for move in UD:
                m_r, m_c = move
                new_r, new_c = r + m_r, c + m_c

                if 0 <= new_r < N and 0 <= new_c < M and shape == graph[new_r][new_c] and not visit[new_r][new_c]:
                    q.append((new_r, new_c))

    return 1


if __name__ == '__main__':
    N,M = map(int,input().split())
    graph = [list(input().strip()) for _ in range(N)]
    visit = [[0]*M for _ in range(N)]
    UD = [(-1,0),(1,0)]
    LR = [(0,-1),(0,1)]
    answer = 0


    while(1):
        start_idx = find_not_visit(N,M)

        if start_idx == -1:
            print(answer)
            break
        else:
            r,c = start_idx
            answer += bfs(N,M,r,c)







