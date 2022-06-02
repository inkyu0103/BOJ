# 12100

'''
2048 최대 5번 이동시켜서 얻을 수 있는 가장 큰 블록 출력

필요한 조건들 : 그리고 각 상태에 대한 기억이 필요함.

puzzle에 대해서 각 단계별로 가지고 있어야 할듯?
depth와 puzzle

depth가 5가되면, 최댓값을 리턴한다.

- 점수 합치기
    - 똑같은 아이들이 여러개 있는 경우, 이동하려고 하는 쪽의 칸이 먼저 합쳐진다.
- 다음 움직임
- 한번의 이동에 합쳐진 블록은 다시 합쳐질 수 없다. (이동 로직에 추가)

- 움직이는 조건을 생각해보자
    1. 옆에 블럭이 없는 경우 (그냥 옮기기)
    2. 옆에 자신과 같은 블럭이 있는데, 합쳐진 적이 없는 경우
    3. 옆에 자신과 같은 블럭이 있는데, 합쳐진 적이 있는 경우 -> 그대로
    4. 옆에 자신과 다른 불럭이 있는 경우 -> 그대로

    최종 위치에서 합쳐진 경우가 있는지에 대한 정보가 필요할 듯 하다.
'''

import sys
input = sys.stdin.readline

def find_max_score(puzzle):
    result = 0
    for r in range(len(puzzle)):
        for c in range(len(puzzle)):
            result = max(result,puzzle[r][c])

    return result


def move_left(puzzle,union):
    length = len(puzzle)
    for r in range(length):
        for c in range(1,length):
            if puzzle[r][c]:
                while c != 0:
                    if puzzle[r][c-1] == 0:
                        puzzle[r][c-1] = puzzle[r][c]
                        puzzle[r][c] = 0

                    if puzzle[r][c] == puzzle[r][c-1] and not union[r][c-1]:
                        puzzle[r][c-1] = puzzle[r][c] * 2
                        puzzle[r][c] = 0
                        union[r][c-1] = 1

    return puzzle,union



def move_right(puzzle,union):
    length = len(puzzle)
    for r in range(length):
        for c in range(length-1):
            if puzzle[r][c]:
                while c != length-1 and puzzle[r][c + 1] == puzzle[r][c]:
                    puzzle[r][c + 1] *= 2
                    puzzle[r][c] = 0
                    c -= 1
    return puzzle

def move_up(puzzle,union):
    length = len(puzzle)
    for r in range(1,length):
        for c in range(length):
            if puzzle[r][c]:
                while r != 0 and puzzle[r-1][c] == puzzle[r][c]:
                    puzzle[r-1][c] *= 2
                    puzzle[r][c] = 0
                    r -= 1
    return puzzle

def move_down(puzzle,union):
    length = len(puzzle)
    for r in range(length-1):
        for c in range(length):
            if puzzle[r][c]:
                while r != 0 and puzzle[r+1][c] == puzzle[r][c]:
                    puzzle[r+1][c] *= 2
                    puzzle[r][c] = 0
                    r -= 1
    return puzzle


def backtrack(depth,puzzle,union):
    result = 0
    # base case
    if depth == 5:
        return find_max_score(puzzle)

    # each direction
    for dir_function in [move_down,move_up,move_left,move_right]:
        result = max(result,backtrack(depth+1,dir_function(puzzle,union)))

    return result

def sol():
    N = int(input())
    puzzle = [list(map(int,input().split())) for _ in range(N)]
    union = [[0]*N for _ range(N)]
    print(backtrack(0,puzzle))

sol()
