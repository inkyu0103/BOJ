# 아기상어 (시작시간 10시 50분 ~ 30분 경과 / 첫 완료 11시 35분 :45분)
from collections import deque,defaultdict
import sys
input = sys.stdin.readline

def find_loc () :
    for r in range(N):
        for c in range(N):
            if graph[r][c] == 9:
                return (r,c)

# bfs 가 어떤 역할을 하는지알아야한다. --> 다음 먹이 위치를 가르쳐 준다.

def bfs(shark):
    visit= [[0]*N for _ in range(N)]
    dist = [[0]*N for _ in range(N)]
    visit[shark[0]][shark[1]] = 1
    fish = []
    q = deque([0,shark[0],shark[1]])

    while q:
        r,c = q.popleft()

        for dr,dc in dirs:
            new_r,new_c = r+dr,c+dc

            if 0<= new_r<N and 0<=new_c<N and not visit[new_r][new_c]:
                if graph[new_r][new_c] <= graph[r][c] or not graph[new_r][new_c]:
                    q.append((new_r,new_c))
                    dist[new_r][new_c] = dist[r][c] + 1
                    visit[new_r][new_c] = 1
                if graph[new_r][new_c]<graph[r][c] and graph[new_r][new_c]:
                    fish.append((dist[new_r][new_c],new_r,new_c))

    if not fish:
        return -1,-1,-1

    fish.sort(key = lambda:x())












if __name__=='__main__':
    N = int(input())
    graph = [list(map(int,input().split())) for _ in range(N)]
    dirs = [(0,1),(0,-1),(1,0),(-1,0)]
    shark = find_loc()





