# 로봇 청소기
# 테스트 케이스는 돌아감
import sys

# 북 동 남 서
dirs = [(-1,0),(0,1),(1,0),(0,-1)]

# 왼쪽을 돌아본다? 자신의 방향에서 -1 하면 됨
def sol():
    count = 0
    clean_room = 1 #첫 번째 방은 무적권 청소임
    row_size,col_size = map(int,sys.stdin.readline().split())
    init_r, init_c,init_d = map(int,sys.stdin.readline().split())
    graph = [[int(i) for i in sys.stdin.readline().split()] for _ in range(row_size)]

    # while문을 돌리고 탈출하는 조건을 따지자.
    while(1):
        # 왼쪽으로 틀자
        init_d -= 1
        if init_d <0 :
            init_d = 3

        # 범위 안에 들어온다면
        if 0<=init_r+dirs[init_d][0]<row_size and 0<=init_c+dirs[init_d][1]<col_size:
            # 청소했는지 확인하자
            # 청소를 안했다면, 이동시키자.
            # 청소 안한곳은 0 벽은 1, 한 곳은 2
            if not graph[init_r+dirs[init_d][0]][init_c+dirs[init_d][1]]:
                init_r += dirs[init_d][0]
                init_c += dirs[init_d][1]
                # 청소 완료 했습니다~
                graph[init_r][init_c] = 2
                clean_room += 1

                # 돌아본 횟수 초기화
                count = 0
                continue

            # 벽이거나, 청소를 한 경우
            else:
                count += 1
        # 범위안에 들어오지 않는다면?
        else:
            count += 1

        # 4곳 모두 둘러본 경우 현 방향을 유지한 채로 한칸 후진
        if count == 4:
            if 0<=init_r-dirs[init_d][0]<row_size and 0<=init_c-dirs[init_d][1]<col_size:
                # 뒤가 벽일 때
                if graph[init_r-dirs[init_d][0]][init_c-dirs[init_d][1]] == 1:
                    break

                elif graph[init_r-dirs[init_d][0]][init_c-dirs[init_d][1]] == 2:
                    init_r -= dirs[init_d][0]
                    init_c -= dirs[init_d][1]
                    count = 0
                    continue
sol()
