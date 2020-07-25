# 11199 오일러 회로

'''
오일러 경로가 불가능한 경우

1. 차수가 홀수인 경우
주의 :  Component 문제 : 그래프의 정점이 둘 이상의 컴포넌트로 쪼개져 있더라도, 간선들이 한 컴포넌트에 있기만 한다면 오일러 서킷 존재.

컴포넌트가 여러개로 갈리는 경우

-다른 컴포넌트에 간선만 없으면 오일러 경로는 존재한다

- 노드가 1개만 있는 경우는
'''

import sys

vertex = int(input())
visited = [False]*vertex

Graph = [list(map(int,sys.stdin.readline().split())) for _ in range(vertex)]
circuit = []
print(Graph)

def dfs(start):
    global counter
    #방문했어요!
    visited[start]=True
    counter += 1

    # 방문하지 않은 노드가 있다면 방문하도록 할게요
    for i in range(vertex):
        if Graph[start][i]:
            Graph[start][i] -=1
            Graph[i][start] -=1
            dfs(i)

    # 재귀함수가 끝날때 기록할게요
    circuit.append(start+1)


def Euler(start):
    # 노드의 차수가 짝수가 아닌 경우
    for i in Graph:
        if sum(i)%2 !=0:
            return -1

    #dfs (무조건 1번노드에서 찍자)
    dfs(start)
    return

val = Euler(0)
counter = 0

flag = 0
for i in range(len(visited)):
    if not visited[i]:
        dfs(i)

        if counter >=2 :
            flag = 1




if val == -1 :
    print(-1)
else:
    for i in circuit:
        print(i,end=" ")

