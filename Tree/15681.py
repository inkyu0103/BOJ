# 15681 트리와 쿼리
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def sol():
    # R is root Num
    N,R,Q = map(int,input().split())
    graph = [[] for _ in range(N+1)]
    parent = [[] for _ in range(N+1)]
    child = [[] for _ in range(N+1)]
    size = [1]*(N+1)

    # making graph
    for _ in range(N-1):
        s,e = map(int,input().split())
        graph[s].append(e)
        graph[e].append(s)

    def makeTree(curNode, parentNode):
        for nextNode in graph[curNode]:
            if nextNode != parentNode:
                # 우리 아이
                child[curNode].append(nextNode)
                # 우리 부모
                parent[nextNode].append(curNode)
                makeTree(nextNode, curNode)

    def countSubTree(curNode):
        for nextNode in child[curNode]:
            countSubTree(nextNode)
            size[curNode] += size[nextNode]


    makeTree(R,-1)
    countSubTree(R)

    for _ in range(Q):
        val = int(input())
        print(size[val])


sol()





