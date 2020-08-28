#12865
import sys


def solve ():
    for i in range(1,num+1):
        for j in range(1,endure+1):
            if box[i-1][0] <= j:
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-box[i-1][0]]+box[i-1][1])
            else:
                dp[i][j] = dp[i-1][j]





num,endure = map(int,sys.stdin.readline().split())

box =[]

for i in range(num):
    weight , value = map(int,sys.stdin.readline().split())
    box.append((weight,value))

dp = [[0]*(endure+1) for _ in range(num+1)]
solve()

print(dp[num][endure])







