#9081 _re
from collections import deque
import sys
input = sys.stdin.readline

def sol():
    N = int(input())

    def bfs():
        visit = set()
        visit.add("")

        q = deque()
        q.append([0,0,""])

        while q:
            f,s,cur_word=q.popleft()

            if f<len(first) and s<len(second):

                if cur_word+first[f] == third or cur_word+second[s] == third:
                    return True

            if f<len(first)-1 and cur_word+first[f] not in visit:
                visit.add(cur_word+first[f])
                q.append([f+1,s,cur_word+first[f]])

            if s<len(second)-1 and cur_word+first[s] not in visit:
                visit.add(cur_word+second[s])
                q.append([f,s+1,cur_word+second[s]])

        return False







    for _ in range(N):
        first, second, third = map(str, input().strip().split())
        val = bfs()
        print(val)





sol()