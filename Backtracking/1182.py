# 1182
import sys
input = sys.stdin.readline

def sol():
    N,S = map(int,input().split())
    sequence = list(map(int,input().split()))
    initial_sum  = 0
    visit = [0] * N
    answer = 0

    def backtrack(depth,max_depth,partial_sum,start=0):
        # base case
        if depth == max_depth and partial_sum == S:
            return 1

        if depth == max_depth:
            return 0

        count = 0

        for x in range(start,N):
            if not visit[x]:
                visit[x] = 1
                count += backtrack(depth+1,max_depth ,partial_sum + sequence[x],x+1)

                visit[x] = 0

        return count

    for i in range(1,N+1):
        answer += backtrack(0,i,initial_sum)

    print(answer)

sol()