# 12100 2048 브루트 포스?
# 시작 시간 2:21 ~ 첫 제출 (4:23)  아니... 2시간동안 했다고?? 근데 3% 컷. ''ㅇ''...
'''
5번 이동시켜서 얻을 수 있는 가장 큰 블록
전역 변수처럼 취급이 되는데...
'''

import sys
import copy
input = sys.stdin.readline

def rotate(table,d,cnt):
    global max_val
    if cnt == 5 :
        return

    change_flag = 0

    if d == "L":
        for j in range(1,N):
            for i in range(N):
                # 현재 값이 존재할 때만 적용
                if table[i][j]:

                    # 앞과 같을 때
                    if table[i][j-1] == table[i][j]:
                        change_flag = 1
                        table[i][j-1] *=2
                        table[i][j] = 0


                    #이전 블럭이 빈 경우 (0)
                    elif not table[i][j-1]:
                        change_flag = 1

                        tmp_j = j
                        # 예외케이스 발생 주의 --> tmp_j == 0 인경우 or table[i][tmp_j-1]이 있는 경우
                        while tmp_j>0 and not table[i][tmp_j-1]:
                            tmp_j -= 1

                        if tmp_j == 0:
                            table[i][tmp_j] = table[i][j]

                        elif table[i][tmp_j-1] == table[i][j]:
                            table[i][tmp_j-1] *=2

                        else:
                            table[i][tmp_j] = table[i][j]

                        table[i][j] = 0



    elif d == "R":
        for j in range(N-2,-1,-1):
            for i in range(N):
                if table[i][j] :
                    # 같은 경우
                    if table[i][j] == table[i][j+1]:
                        table[i][j+1] *= 2
                        change_flag = 1
                        table[i][j] = 0

                    # 블럭이 빈경우
                    elif not table[i][j+1]:
                        change_flag = 1

                        tmp_j = j

                        while tmp_j < N-1 and not table[i][tmp_j+1]:
                            tmp_j += 1


                        if tmp_j == N-1:
                            table[i][tmp_j] = table[i][j]
                        elif table[i][tmp_j+1] == table[i][j]:
                            table[i][tmp_j+1] *= 2
                        else:
                            table[i][tmp_j] = table[i][j]
                        table[i][j] = 0



    elif d == "U":
        for i in range(1,N):
            for j in range(N):
                if table[i][j] :
                    if table[i][j] == table[i-1][j]:
                        table[i-1][j] *= 2
                        change_flag = 1
                        table[i][j] = 0



                    elif not table[i-1][j]:
                        change_flag = 1

                        tmp_i = i
                        while tmp_i > 0 and not table[tmp_i-1][j]:
                            tmp_i -= 1

                        if tmp_i == 0:
                            table[tmp_i][j] = table[i][j]

                        elif table[tmp_i-1][j] == table[i][j]:
                            table[tmp_i-1][j] *= 2

                        else:
                            table[tmp_i][j] = table[i][j]
                        table[i][j] = 0



    elif d == "D":
        for i in range(N-2,-1,-1):
            for j in range(N):
                if table[i][j]:
                    if table[i][j] == table[i + 1][j]:
                        table[i + 1][j] *= 2
                        change_flag = 1
                        table[i][j] = 0



                    elif not table[i + 1][j]:
                        change_flag = 1

                        tmp_i = i
                        while tmp_i < N-1 and not table[tmp_i + 1][j]:
                            tmp_i += 1

                        if tmp_i == N-1:
                            table[tmp_i][j] = table[i][j]

                        elif table[tmp_i +1][j] == table[i][j]:
                            table[tmp_i + 1][j] *= 2
                        else:
                            table[tmp_i][j] = table[i][j]
                        table[i][j] = 0
    print('cnt :',cnt,"d",d)
    for i in table:
        print(i)

    print("------------------------")

    if not change_flag:
        return

    for i in range(N):
        for j in range(N):
            max_val = max(max_val,table[i][j])


    tmp_table = copy.deepcopy(table)
    for d in dirs:
        rotate(tmp_table,d,cnt+1)



if __name__ == '__main__':
    N = int(input())
    table = [list(map(int,input().split(" "))) for _ in range(N)]
    dirs = ["L","R","U","D"]
    max_val = -1

    for d in dirs:
        # 메모리 초과가 뜨지는 않을까?
        copy_table = copy.deepcopy(table)
        rotate(copy_table,d,0)

    print(max_val)

