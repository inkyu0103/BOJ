# 인구이동 (시작시간 11시 54분) 1차시간 12시 반
# 생각 12시 반 ~ 1시
'''
국경선이 열린 부분을 어떻게 판단?
순회를 통해서 어디까지 움직이는지 봐야할듯?

컴포넌트가 여러개일까? ( 연합이 1개 이상인가? )
인구이동이 되면서 여러개의 연합이 1개로 연합되는 경우가 존재하는가?
경계를 공유하는 모든 나라의 인구차이

어려운 점 : 1일 내에 한꺼번에 같이 갱신되어야 하는데, 그걸 어떻게 표현할지가 문제.
종료조건 : 한 번도 국경이 열리지 않으면 빠빠이 이렇게하면 탐색과정에서도 문젠데.
'''

import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    print(L,R)
    q = deque([start])
    tmp = [start]

    while q:
        r,c = q.popleft()


        for d in dirs:
            dr,dc = d
            new_r,new_c = r+dr,c+dc

            if 0<= new_r <N and 0<= new_c <N  and not visit[new_r][new_c]:
                if L<=abs(graph[r][c] - graph[new_r][new_c])<=R:
                    visit[new_r][new_c] = 1
                    q.append((new_r,new_c))
                    tmp.append((new_r,new_c))
    return tmp


if __name__ =="__main__":
    N,L,R = map(int,input().split())
    graph = [list(map(int,input().split())) for _ in range(N)]
    dirs = [(0,1),(0,-1),(1,0),(-1,0)]

    count = 0
    while 1:
        visit = [[0]*N for _ in range(N)]
        flag = 0

        for r in range(N):
            for c in range(N):
                if not visit[r][c]:
                    visit[r][c] = 1
                    val = bfs((r,c))

                    # 추가된 국가가 있는 경우
                    if len(val) > 1 :
                        flag = 1
                        even = sum([graph[r][c] for r,c in val])//len(val)

                        for r,c in val:
                            graph[r][c] = even

        if not flag:
            break
        count += 1

    print(count)
