# 1254
import sys
input = sys.stdin.readline

def sol():
    s = input().rstrip()
    for i in range(len(s)):
        if s[i:] == s[i:][::-1]:
            print(len(s) + i)
            return
sol()
