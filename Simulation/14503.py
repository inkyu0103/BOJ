# 로봇 청소기
import sys

def sol():
    # 북, 동, 남, 서 (-1이 왼쪽을 가리킨다)
    dirs = [(1,0),(0,1),(-1,0),(0,-1)]

    # 처음 있는 곳은 청소가 되어있지 않기 때문
    count = 1

    # 네 방향이 모두 벽인지 확인하는 플래그
    flag = 0

    # N : 가로(row) , M : 세로 (col)
    N,M = map(int,sys.stdin.readline().split())
    init_r, init_c, direction = map(int,sys.stdin.readline().split())
    space = [[int(i) for i in sys.stdin.readline().split()] for i in range(N)]
    # 처음 있는 자리는 깨끗하게 청소 ~
    space[init_r][init_c] = 2
    '''    
        현재 위치에서 현재 방향을 기준으로 왼쪽방향부터 차례대로 탐색을 진행한다. -1을 하는데 음수가 뜨면 
        왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
        왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 2번으로 돌아간다.
        네 방향 모두 청소가 이미 되어있거나 벽인 경우에는, 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
        네 방향 모두 청소가 이미 되어있거나 벽이면서, 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.
        
        벽이랑 청소를 한 곳이랑 따로 구분해야 하는구나.
    '''
    # 이게 맞을까...
    while(1):
        print("my dir is : {} ".format(direction))
        # 네 방향이 모두 벽인지 아닌지 확인하는 플래그
        flag = 0

        # 네 방향이 모두 벽인지 확인 이거를 어떻게 확인하는거야
        for i in dirs:
            if space[init_r + i[0]][init_c+i[1]] == 0 or space[init_r + i[0]][init_c+i[1]] == 2:
                flag = 1
                break

        # 오 네 방향이 모두 벽은 아니네!
        if flag == 1:
            # 방향 회전
            direction -= 1

            # 만약 빼고 나서 음수가 된 경우 (초기에 0이었던 경우)
            if direction < 0:
                direction = 3

            #탐색
            if 0 <= init_r + dirs[direction][0] < N and 0 <= init_c + dirs[direction][1] < M:
                # 만약 진행 방향의 값이 벽인 경우
                if space[init_r + dirs[direction][0]][init_c + dirs[direction][1]] == 1:
                    #회전만 하게 됨
                    continue
                # 벽이 아닌 경우
                else:
                    # 그 쪽으로 한칸 앞으로 이동
                    init_r += dirs[direction][0]
                    init_c += dirs[direction][1]

                    #청소 했습니다~
                    space[init_r][init_c] = 2

                    # 청소한 구역 1칸 증가
                    count += 1
                    continue

        # 아이고 모두 벽이네;
        elif flag == 0:
            print("마 모두 벽이야!")
            # 현재 바라보는 방향으로 한칸 후진이 되니...?
            if 0<= init_r - dirs[direction][0]< N and 0<= init_c - dirs[direction][1] < M:
                if space[init_r-dirs[direction][0]][init_c-dirs[direction][1]] == 0:
                    init_r -= dirs[direction][0]
                    init_c -= dirs[direction][1]
                    count += 1

                elif space[init_r-dirs[direction][0]][init_c-dirs[direction][1]] == 2:
                    init_r -= dirs[direction][0]
                    init_c -= dirs[direction][1]

                # 안되니..?
                else:
                    print("아뇨... 후진은 안되는뎁셔...")
                    # 작동을 멈추거라
                    break

    print(count)
sol()