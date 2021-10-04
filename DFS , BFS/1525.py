# 1525 퍼즐 - 아이디어
from collections import deque
import sys
input = sys.stdin.readline

def sol():
    def bfs(dist,zero_loc,start):
        if start == '123456780':
            return 0

        visit = set()
        visit.add(start)

        q = deque()
        q.append([dist,zero_loc,start])

        while q:
            cur_dist,cur_zero_loc,cur_start = q.popleft()

            for d in dirs:
                if 0<=cur_zero_loc + d<9:
                    new_graph = list(cur_start)
                    new_graph[cur_zero_loc],new_graph[cur_zero_loc+d] = new_graph[cur_zero_loc+d],new_graph[cur_zero_loc]

                    new_graph = "".join(new_graph)
                    print(new_graph,cur_zero_loc+d)

                    if new_graph == '123456780':
                        return cur_dist+1

                    if new_graph not in visit:
                        visit.add(new_graph)
                        q.append([cur_dist+1,cur_zero_loc+d,new_graph])

        return -1

    graph = []

    dirs = [1,-1,3,-3]

    for _ in range(3):

        graph += list(map(str,input().strip().split()))

    zero_idx = graph.index('0')

    print(bfs(0,zero_idx,"".join(graph)))


sol()