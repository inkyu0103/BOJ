# 17141 연구소 2
'''
1. 바이러스를 놓는 후보 칸 존재 --> 바이러스가 없는 후보칸을 고르자
(왜냐하면 map 을 복사할 것이기 때문)
'''

from collections import deque
from itertools import combinations
import copy
import sys
input = sys.stdin.readline

# 단순 copy시 list 내부에 object가 있는 경우 주의할 것
def sol():
    def bfs():

        visit = [[0]*N for _ in range(N)]
        q = deque()

        for r in range(N):
            for c in range(N):
                if target_map[r][c] == 2:
                    visit[r][c] = 0
                    q.append([0,r,c])

        while q:
            time,r,c = q.popleft()

            for dr,dc in dirs:
                new_r ,new_c = r+dr,c+dc

                # 새로 도달하는 곳이 벽이 아닌 경우 ( visit의 여부를 조건으로 넣지 않은 이유는
                # virus가 뻗어나갈때 visit 조건을 달면 무조건 지나치기 때문

                if 0<=new_r<N and 0<=new_c<N and target_map[new_r][new_c] != 1:

                    # 1. 빈 공간인 경우
                    if not target_map[new_r][new_c] and not visit[new_r][new_c]:
                        q.append([time+1,new_r,new_c])
                        visit[new_r][new_c] = time+1
                        target_map[new_r][new_c] = 2

                    # 2. 바이러스인 경우
                    elif target_map[new_r][new_c] == 2:
                        # 내가 더 빨리 도달할 수 있는 경우에만 갱신
                        if visit[new_r][new_c] > time + 1:
                            q.append([time+1,new_r,new_c])
                            visit[new_r][new_c] = time + 1



        # 빈 공간이 있나 체크

        result = 0

        for r in range(N):
            for c in range(N):
                if not target_map[r][c]:
                    return -1
                else:
                    result = max(result,visit[r][c])



        return result


    N,M = map(int,input().split())
    _map = [list(map(int,input().split())) for _ in range(N)]
    viruses  =[]
    dirs = [(0,1),(0,-1),(1,0),(-1,0)]

    # 바이러스 후보군 추가
    for r in range(N):
        for c in range(N):
            if _map[r][c] == 2:
                viruses.append([r,c])

    result = -1

    # 바이러스 후보칸에서 제외할 대상 뽑기
    for target in combinations(viruses,len(viruses)-M):

        target_map = copy.deepcopy(_map)

        # 바이러스 후보에서 제외 --> 빈 칸 --> 이렇게 하면 bfs가 복잡해진다.
        for r,c in target:
           target_map[r][c] = 0

        # 이렇게 두면 -1 한 번 나오면 계속 고정된다.
        val = bfs()

        if result == -1 and val != -1:
            result = val

        elif result != - 1 and val != -1:
            result = min(result,val)



    print(result)

sol()
