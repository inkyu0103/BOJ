#1633
import sys
input = sys.stdin.readline

def sol():
    people = []
    while 1:
        info = list(map(int,input().split()))
        if not info:
            break

        people.append(info)

    length = len(people)
    dp = [[[0]*16 for _ in range(16)] for _ in range(length+1)]

    for i in range(length):
        for w in range(16):
            for b in range(16):
                if w+1<=15:
                    dp[i+1][w+1][b] = max(dp[i+1][w+1][b],dp[i][w][b] + people[i][0])

                if b+1 <= 15:
                    dp[i+1][w][b+1] = max(dp[i+1][w][b+1],dp[i][w][b] + people[i][1])

                dp[i+1][w][b] = max(dp[i+1][w][b],dp[i][w][b])


    print(dp[length][15][15])

sol()






'''
1. 30명 제한
2. Dynamic 
'''