# 11403 경로 찾기
'''
1. i -> j 로 가는 것이 있는 지 없는지는 dfs를 돌려보면 된다

2. i -> i 로 가는 경로가 있는지는 뭘로 확인하나?

'''
import sys

vertex = int(sys.stdin.readline())

graph = [list(map(int,sys.stdin.readline().split())) for _ in range(vertex)]
answer = [[0]*vertex for _ in range(vertex)]

visit = [False]*vertex

def dfs(start):

    visit[start] = True

    for i in range(vertex):
        if graph[start][i] and visit[i] == False:
            answer[start][i] = 1
            dfs(i)

dfs(0)

print(answer)












