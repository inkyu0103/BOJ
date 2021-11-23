# 5427

'''
매 초마다 불은 동서남북 방향으로 퍼져나간다.

벽에는 불 안붙음

상근이도 동서남북으로 간다.

상근이는 불이 옮겨진 칸 또는 이제 불이 붙으려는 칸 이동 불가

불 -> 상근 순으로 움직이면 되지 않을까?

불은 이동할 때 이전 부분이 꺼질 필요가 없으니, visit은 사람만 표시하는 것으로 하자.

탈출 성공 조건이 매우 웃긴다.

human의 조건이 범위를 넘어가는 경우에만 가능.

아 처음에 불과 사람을 -1 -1 로 둬서 그렇구나?

흠... 그래서 사람을 먼저 움직이나?
'''

import sys
from collections import deque
input = sys.stdin.readline

def sol():
    dirs = [(0,1),(0,-1),(1,0),(-1,0)]
    def find_start():
        # -1로 둔 부분이 문제, 만약 불이 없는 경우는 어떻게 할래?
        fire, human = (-1, -1), (-1, -1)
        for r in range(h):
            for c in range(w):
                if _map[r][c] == "@":
                    human = (r,c)
                elif _map[r][c] == "*":
                    fire = (r,c)
        return fire,human

    def bfs(fr, fc, hr, hc):

        visit = [[0]*w for _ in range(h)]
        fq = deque([[fr,fc]]) if [fr,fc] != [-1,-1] else deque([])
        hq = deque([[0,hr,hc]])

        fire_pop_count = len(fq)
        human_pop_count = len(hq)
        visit[hr][hc] = 1

        while fire_pop_count or human_pop_count:
            while fire_pop_count:
                cur_fr,cur_fc = fq.popleft()
                fire_pop_count -= 1

                for dr,dc in dirs:
                    new_fr,new_fc = cur_fr + dr , cur_fc + dc
                    if 0<= new_fr < h and 0<= new_fc < w and _map[new_fr][new_fc] in ["@","."]:
                        fq.append([new_fr,new_fc])
                        _map[new_fr][new_fc] = '*'
            fire_pop_count = len(fq)

            # 불이 한 번 움직이고 , 이제 사람이 움직일 차례

            while human_pop_count:
                step,cur_hr,cur_hc = hq.popleft()

                if (cur_hr in [0, h - 1] or cur_hc in [0, w - 1]):
                    return step

                human_pop_count -= 1

                for dr,dc in dirs:
                    new_hr,new_hc = cur_hr+dr, cur_hc + dc

                    #탈출구일때
                    if (new_hr in [0,h-1] or new_hc in [0,w-1]) and _map[new_hr][new_hc] == '.':
                        return step + 2

                    #탈출구는 아닐 때 -> 현재 위치가 불인지 확인하고 지워야함
                    elif 0<new_hr<h and 0<new_hc<w and _map[new_hr][new_hc] == '.' and not visit[new_hr][new_hc]:
                        _map[new_hr][new_hc] = '@'
                        hq.append([step+1,new_hr,new_hc])
                        visit[new_hr][new_hc] = 1

                if _map[cur_hr][cur_hc] == '@':
                    _map[cur_hr][cur_hc] = '.'

            human_pop_count = len(hq)

        return -1

##############################################################
    tc = int(input())
    for _ in range(tc):
        w,h = map(int,input().split())
        _map = [list(input().strip()) for _ in range(h)]
        s_fire,s_human = find_start()
        result = bfs(*s_fire,*s_human)
        print(result if result != -1 else "Impossible")

sol()
