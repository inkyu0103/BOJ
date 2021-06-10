# 4803

import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

'''
 뭔가 순서가 잘못된 것 같은데
'''

def dfs(curNode,beforeNode):
    visit[curNode] = 1
    for nextNode in graph[curNode]:
        if nextNode == beforeNode:
            continue
        elif visit[nextNode]:
            return False
        elif not dfs(nextNode,curNode):
            return False

    return True







if __name__ == "__main__":
    case = 1

    while 1:
        n, m = map(int, input().split())
        numTree = 0
        visit = [0] * (n + 1)

        if n == 0 and m == 0:
            break

        graph = [[] for _ in range(n + 1)]


        for _ in range(m):
            s, e = map(int, input().split())
            graph[s].append(e)
            graph[e].append(s)

        for node in range(1, n + 1):
            if not visit[node] and dfs(node,0):
                numTree += 1

        if numTree == 0:
            print("Case {}: No trees.".format(case))

        elif numTree == 1:
            print("Case {}: There is one tree.".format(case))

        else:
            print("Case {}: A forest of {} trees.".format(case,numTree))

        case += 1
