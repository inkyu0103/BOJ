# 상어 초등학교
import sys
from collections import defaultdict
input = sys.stdin.readline

# 첫 번째 조건 : 한 점에서 인접한 자리에 자신이 좋아하는 사람이 가장 많은 점

def first_condition():
    adj_friends_map =defaultdict(list)

    for r in range(N):
        for c in range(N):
            # 그 자리에 이미 숫자가 있다면 --> 넘어가자
            if seats[r][c]:
                continue

            adj_friends_num = 0
            for move in dirs:
                move_r, move_c = move
                new_r, new_c = r+move_r, c+move_c

                # 인접한 곳에 친구들이 있으면...
                if 0<= new_r < N and 0<= new_c < N and seats[new_r][new_c] in students_info[student_num]:
                    adj_friends_num += 1

            adj_friends_map[adj_friends_num].append((r,c))

    return adj_friends_map[max(adj_friends_map)]

def second_condition():



if __name__ =='__main__':
    N = int(input())
    seats = [[0]*N for _ in range(N)]
    dirs = [(0,1),(1,0),(0,-1),(-1,0)]

    students_info = {}
    for _ in range(N**2):
        student_num , *like_friends = map(int,input().split())
        students_info[student_num] = like_friends

        first_condition_result = first_condition()

        if len(first_condition_result) == 1:
            seats[first_condition_result[0][0]][first_condition_result[0][1]] = student_num

        else:
            second_condition(first_condition_result)






