# 11722 가장 긴 감소하는 부분수열

num = int(input())
seq = [int(i) for i in input().split()]
dp = [-1]*num

def solve(start):
    if dp[start] != -1:
        return dp[start]

    for i in range(start,num):
        ret = 1
        for j in range(i+1,num):
            if(seq[i]>seq[j]):
                ret = max(ret,solve(j)+1)
        dp[start] = ret
        return ret

solve(0)
for i in range(num):
    if dp[i] == -1:
        solve(i)

print(max(dp))
