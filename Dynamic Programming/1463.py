#1463 1로 만들기

num = int(input())

dp = [-1]*(num+1)

def solve(num):
    if num == 1:
        return 0
    elif num == 2:
        return 1
    elif num == 3:
        return 1
    else:
        dp[1] = 1
        dp[2] = 1
        dp[3] = 1
        for i in range(4,num+1):
            # 만약 초기화 되지 않았다면,
            if dp[i] == -1:

                # 2와 3 둘다 나뉘는 경우
                if i%3 == 0 and i % 2 == 0:
                    dp[i] = min(dp[int(i/3)],dp[int(i/2)],dp[i-1]) + 1
                #그리고 그게 3으로만 나뉜다면
                elif i % 3 == 0:

                    dp[i] = min(dp[int(i/3)],dp[i-1]) + 1
                #또는 2로 나누어진다면
                elif i % 2 == 0:
                    dp[i] = min(dp[i-1], dp[int(i/2)]) + 1
                # 또는 아무 조건에 해당하지 않는다면
                else :
                    dp[i] = dp[i-1] + 1

        return dp[num]

            #만약 초기화 되었다면...넘어가면 된다?

            # 1을 더해주는 이유는 한 번 더 연산을 하니까

print(solve(num))



