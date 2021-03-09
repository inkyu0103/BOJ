# 1992 쿼드트리

import sys
input = sys.stdin.readline

def sol (startR,startC,length):
    global answer
    check = Tree[startR][startC]
    for i in range(startR,startR+length):
        for j in range(startC,startC+length):
            if check != Tree[i][j]:
                answer += "("
                sol(startR,startC,length//2)
                sol(startR,startC+length//2,length//2)
                sol(startR+length//2,startC,length//2)
                sol(startR+length//2,startC+length//2,length//2)
                answer += ")"
                return
    if check == "1":
        answer += "1"
    else:
        answer += "0"


if __name__ == "__main__":
    size = int(input())
    Tree = [[*(input().strip())] for _ in range(size)]
    answer = ""
    sol(0,0,size)
    print(answer)
