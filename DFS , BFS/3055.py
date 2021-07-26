# 3055 탈출
 '''
주의해야 할 것. 각각 한 턴씩 움직일 수 있는가?
고슴도치가 움직일 수 있는 범위에 대해서 움직인다 --> 물이 움직일 수 있는 범위에 대해서 움직인다.

추가되는 부분에 대해서는 다음 분기에 처리해야한다.
 '''


import sys
from collections import deque
input = sys.stdin.readline


def bfs():





if __name__ =="__main__":
    R,C = map(int,input().split())
    D,S,W = (-1,-1),(-1,-1),(-1,-1)
    dirs = [(0,1),(0,-1),(1,0),(-1,0)]
    visit = [[0]

    graph = []
    for r in range(R):
        tmp = list(input().strip())
        for c in range(C):
            if tmp[c] =="D":
                D = (r,c)
            elif tmp[c]== "*":
                W = (r,c)
            elif tmp[c] == "S":
                S = (r,c)





