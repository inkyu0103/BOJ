# 11266 단절점
import sys
input = sys.stdin.readline

def dfs():
    

def sol():
    V,E = map(int,input().split())
    graph = [[] for _ in range(V)]
    visit =[-1] * V

    for i in range(E):
        s,e = map(int,input().split())
        graph[s].append(e)
        graph[e].append(s)


sol()
