# 2630 색종이 만들기
import sys

def sol(startR, startC , length):
    global blue,white
    check = graph[startR][startC]
    for i in range(startR,startR+length):
        for j in range(startC,startC+length):
            if check != graph[i][j]:
                sol(startR,startC,length//2)
                sol(startR+length//2,startC,length//2)
                sol(startR,startC+length//2,length//2)
                sol(startR+length//2,startC+length//2,length//2)
                return
    if check == 0:
        white += 1
        return
    else:
        blue+=1
        return



if __name__ == "__main__" :
    length = int(sys.stdin.readline())
    graph = [[int(i) for i in sys.stdin.readline().strip().split()] for _ in range(length)]
    blue, white = 0,0
    sol(0,0,length)
    print(white)
    print(blue)




