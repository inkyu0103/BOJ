# 가중치가 같은 간선

import sys

tc = int(input())
for i in range(tc):
    city, airplane = map(int, input().split())
    edge = []
    for j in range(airplane):
        edge.append(list(map(int, sys.stdin.readline().split())))

    print(city - 1)