# 16500 그 문자 섞기랑 비슷한 듯?
import sys
input = sys.stdin.readline

def sol():
    S = input().strip()
    N = int(input())
    words = []

    dp = [0] * (len(S))
    for i in range(N):
        word = input().strip()
        if S.startswith(word):
            dp[len(word)-1] = 1

        words.append(word)

    # 아 마지막 아이.
    for i in range(len(S)-1):
        print(i)
        if dp[i]:
            for word in words:
                print(word)
                if S[i+1:].startswith(word):
                    print(i+len(word))
                    dp[i+len(word)] = 1
    print("1" if dp[-1] else "0" )







    # 최고 100자리 문자열, 1자리 문자 주어질 때



sol()