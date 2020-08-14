# LIS 출력 머리가 안좋으니 힘드네요 ^^

# 일단 가장 긴 수열부터 찾자

seqLength = int(input())
seq = [int(i) for i in input().split()]
dp = [-1]*seqLength


#dp에는 제일 길게 가질 수 있는 수열의 길이를 저장할거에요

def solve(start):
    # 수열의 최소 길이는 1이다.

    # 만약에 그 start번째부터 시작하는 제일 긴 수열이 있다면 ? 그 길이를 반환해 주세요.
    if dp[start] != -1:
        return dp[start]

    ret = 1
    #나는 start부터 검사할래
    for next in range(start+1,seqLength):
        # 만약에 증가하는 값을 발견하면?
        # 일단 거기서부터 시작하는 제일 긴 수열을 찾아본다.
        if seq[start] < seq[next]:
            ret = max(ret,solve(next)+1)
    #반복문을 빠져 나가서 ret를 return 하는 이유 ? 최대값을 뽑아야 하기 때문

    dp[start] = ret
    return ret

solve(0)

print(max(dp))

