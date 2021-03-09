# 1780 종이의 개수

import sys

def sol(startR,startC,length):
    global minus,zero,plus
    check = Tree[startR][startC]
    for i in range(startR,startR+length):
        for j in range(startC,startC+length):
            if check != Tree[i][j]:
                sol(startR,startC,length//3)
                sol(startR,startC+length//3,length//3)
                sol(startR,startC+2*(length//3),length//3)

                sol(startR+length//3, startC, length // 3)
                sol(startR+length//3, startC + length // 3, length // 3)
                sol(startR+length//3, startC + 2 * (length // 3), length // 3)

                sol(startR+2*(length//3), startC, length // 3)
                sol(startR+2*(length//3), startC + length // 3, length // 3)
                sol(startR+2*(length//3), startC + 2 * (length // 3), length // 3)
                return

    if check ==0:
        zero +=1
    elif check == 1:
        plus += 1
    else:
        minus += 1


if __name__ == "__main__":
    input = sys.stdin.readline
    size = int(input())
    Tree = [list(map(int,input().strip().split())) for _ in range(size)]
    minus = 0
    zero = 0
    plus = 0
    sol(0,0,size)
    print(minus)
    print(zero)
    print(plus)
