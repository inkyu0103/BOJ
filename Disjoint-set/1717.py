# 1717 집합의 표현
# simple Union으로 안되네 ㅋㅋ

import sys

def find(node):
    if s[node] == node :
        return node

    else:
        s[node] = s[s[node]]
        return find(s[node])

n,m = map(int, sys.stdin.readline().split())

s = [i for i in range(0,n+1)]

for _ in range(m):
    command,first,second = map(int, sys.stdin.readline().split())

    if command == 0:
        #first의 부모는 second
        s[first] = second


    else:
        if find(first) == find(second):
            print("YES")
        else:
            print("NO")

