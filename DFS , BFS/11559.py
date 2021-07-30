#11559 뿌요뿌요 (시작 시간 2시 40 첫 제출 3:20)
'''
상하 좌우로 4개가 모이면 터짐
여러그룹이 있다면, 한번에 터지는 것으로 실행

'''

from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    bomb_flag = 0
    visit = [[0]*6 for _ in range(12)]
    for r in range(12):
        for c in range(6):
            if field[r][c] != "." and not visit[r][c]:
                bomb_list = [(r,c)]
                visit[r][c] = 1
                q= deque([(r,c)])

                while q:
                    cur_r,cur_c = q.popleft()

                    for dr,dc in dirs:
                        new_r ,new_c = cur_r+dr,cur_c+dc

                        if 0<=new_r<12 and 0<=new_c<6 and field[r][c] == field[new_r][new_c] and not visit[new_r][new_c]:
                            visit[new_r][new_c] = 1
                            q.append((new_r,new_c))
                            bomb_list.append((new_r,new_c))


                # 4개 이상 모이면 펑펑
                if len(bomb_list) >= 4:

                    # 아하 우리 터졌어요 (이렇게 하면 연쇄로도 표현 할 수 있음)
                    bomb_flag = 1
                    for r,c in bomb_list:
                        field[r][c] = '.'


    return bomb_flag



def down():
    for r in range(10,-1,-1):
        for c in range(6):
            if field[r][c] != ".":
                tmp_r = r

                # 등호를 빼는 이유는, tmp_r이 0이고, 맨 바닥이 비어있는 경우에 또  while문이 돌아가서 결국 tmp_r이 -1이 되는 경우가 발생하게 되버린다.
                while tmp_r < 11 and field[tmp_r+1][c] == ".":
                    tmp_r += 1

                if field[tmp_r][c] == '.':
                    field[tmp_r][c] = field[r][c]
                    field[r][c] = '.'









if __name__=='__main__':
    field = [list(input().strip()) for _ in range(12)]
    dirs = [(0,1),(0,-1),(1,0),(-1,0)]
    count = 0


    while 1:
        val = bfs()
        if not val:
            break
        count += 1
        down()


    print(count)