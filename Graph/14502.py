#14502 연구소
'''
가로 세로의 범위가 3<=x<=8 이므로 완전 탐색을 해도 될것 같다.
64C3 해도 4만번 정도만 하면 됨

1. 벽을 세운다 (원래 벽과 겹치지 않아야 한다.)
2. 바이러스를 퍼트린다 (BFS)
3. 감염되지 않은 지역을 찾는다

반복
'''

import sys

row, col = map(int,sys.stdin.readline().split())

# graph
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(row)]

# making wall (어떻게 해야 완전 탐색이 되나요?)
'''
그래프를 넘겨주면 스택에 그대로 있으려나...?
'''
def BFS():
    print(1)


'''
depth는 벽을 세운 횟수
graph는 지금 그래프 모양
roomPoint는 벽을 세울 위치
'''

def making(depth,graph):
    if depth == 3:
        print("벽 3개를 설치하셨어요!")


    else:
       
        for y in range(row):
            for x in range(col):
                if graph[y][x] == 0 :
                    graph[y][x] = 1
                    making(depth+1,graph)
                    graph[y][x] = 0


making(0,graph)


            





