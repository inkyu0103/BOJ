# 2150 scc

'''
    scc 를 찾는 방법

    1. 그래프 G에 대해 DFS 를 한다.

    2. 그래프 G^T 에 대해 DFS 를 한다.


'''

class Node :
    def __init__(self,i):
        self.nodeNum = i
        self.pi = None
        self.stime = None
        self.ftime = None

import sys

if __name__ == "__main__":
    V,E = map(int,sys.stdin.readline().split())
    G = [[] for i in range(V)]
    global_time = 0
    for edge in range(E):
        s,e = map(int,sys.stdin.readline().split())
        node = Node(e-1)
        G[s-1].append(node)







