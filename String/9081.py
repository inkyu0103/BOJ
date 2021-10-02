#9081
from itertools import permutations
import sys
input = sys.stdin.readline

def sol():
    def dfs(f,s,t):
        # 종료 조건?
        if first[f] == third[t] and second[s] != third[t]:
            return dfs(f+1,s,t+1)

        if first[f] != third[t] and second[s] == third[t]:
            return dfs(f,s+1,t+1)

        if first[f] == third[t] and second[s] == third[t]:
            val1 = dfs(f+1,s,t+1)
            val2 = dfs(f,s+1,t+1)

            if val1 or val2:
                return True

            return False

    N = int(input())

    for _ in range(N):

        first,second,third = map(str,input().strip().split())
        result = dfs(0,0,0)
        print(result)


sol()
