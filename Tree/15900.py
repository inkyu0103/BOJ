# 15900
import sys
input = sys.stdin.readline
from collections import deque

def bfs(N,start):
    q = deque([start])
    visited = [0] * (N+1)
    visited[start] = 1
    l_s = 0

    length = 1
    count = 0
    level = 1

    isLeaf = 0

    while q:
        curNode = q.popleft()
        count += 1
        for nextNode in tree[curNode]:
            if not visited[nextNode]:
                q.append(nextNode)
                visited[nextNode] = 1
                isLeaf = 1

        if not isLeaf:
            leaf_node.append(curNode)
            l_s += level - 1

        if length == count :
            count = 0
            length = len(q)
            level += 1

        isLeaf = 0

    return l_s



if __name__=='__main__':
    N = int(input())
    tree = [[] for _ in range(N+1)]
    leaf_node = []

    for _ in range(N-1):
        a,b = map(int,input().split())
        tree[a].append(b)
        tree[b].append(a)
    level_info = bfs(N,1)
    l_s = bfs(N,1)
    # 홀수 레벨은 순서에 영향을 끼치지 않음

    if l_s % 2 != 0:
        print("Yes")
    else:
        print("No")

