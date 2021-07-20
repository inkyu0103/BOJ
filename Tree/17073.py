# 17073 나무위의 빗물  (DFS)
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def DFS(start):
    visit[start]  = 1
    leaf_flag = 0

    for next_node in tree[start]:
        if not visit[next_node]:
            leaf_flag = 1
            DFS(next_node)

    if not leaf_flag:
        leaf_node.append(start)




if __name__ =="__main__":
    N,W = map(int,input().split())
    tree = [[] for _ in range(N+1)]
    visit = [0] * (N+1)
    leaf_node = []
    for _ in range(N-1):
        s,e = map(int,input().split())
        tree[s].append(e)
        tree[e].append(s)

    DFS(1)
    print(W/len(leaf_node))


