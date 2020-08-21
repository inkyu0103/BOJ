#9251_1

firstL = input()
secondL = input()

firstLength = len(firstL)
secondLength = len(secondL)

dp = [[0]* (secondLength+1) for _ in range(firstLength+1)]

for i in range(0,firstLength):
    for j in range(0,secondLength):
        if firstL[i] == secondL[j]:
            dp[i+1][j+1] = dp[i][j] +1

        elif firstL[i] != secondL[j]:
            dp[i+1][j+1] = max(dp[i][j+1],dp[i+1][j])
print(dp[-1][-1])




