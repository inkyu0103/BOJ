# 14891 톱니바퀴
import sys
from collections import deque
input = sys.stdin.readline


def set_state (num,direct):
    direction = [0,0,0,0]
    direction[num] = direct
    if num == 0 :
        if gear_arr[0][2] != gear_arr[1][6]:
            direction[1] = -direction[0]

            if gear_arr[1][2] != gear_arr[2][6]:
                direction[2] = -direction[1]

                if gear_arr[2][2] != gear_arr[3][6]:
                    direction[3] = -direction[2]
    elif num == 1:
        if gear_arr[1][6] != gear_arr[0][2]:
            direction[0] = -direction[1]

        if gear_arr[1][2] != gear_arr[2][6]:
            direction[2] = -direction[1]

            if gear_arr[2][2] != gear_arr[3][6]:
                direction[3] = -direction[2]

    elif num == 2:
        if gear_arr[2][6] != gear_arr[1][2]:
            direction[1] = -direction[2]

            if gear_arr[1][6] != gear_arr[0][2]:
                direction[0] = -direction[1]

        if gear_arr[2][2] != gear_arr[3][6]:
            direction[3] = -direction[2]

    elif num == 3:
        if gear_arr[3][6] != gear_arr[2][2]:
            direction[2] = -direction[3]

            if gear_arr[2][6] != gear_arr[1][2]:
                direction[1] = -direction[2]

                if gear_arr[0][2] != gear_arr[1][6]:
                    direction[0] = -direction[1]
    for i in range(4):
        gear_arr[i].rotate(direction[i])




if __name__ == "__main__":
    gear_arr = [deque(list(map(int,input().strip()))) for _ in range(4)]
    K = int(input())
    answer = 0

    for _ in range(K):
        num , direct = map(int,input().split())
        set_state(num-1,direct)

    for i in range(4):
        answer += (2**i) * gear_arr[i][0]

    print(answer)


