#11053 가장긴

length = int(input())
seq = list(map(int,input().split()))

seq = [-1e20] + seq
dp = [-1]*(length+1)

def solve (start):
    if dp[start] != -1:
        return dp[start]

    dp[start] = 1
    for next in range(start+1,length+1):
        if seq[next] > seq[start]:
            dp[start] = max(dp[start],solve(next)+1)

    return dp[start]

solve(0)
print(max(dp)-1)
