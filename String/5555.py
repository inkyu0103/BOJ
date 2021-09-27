# 5555
import sys
input = sys.stdin.readline

target = input().rstrip()
N = int(input())
arr = [input().rstrip() for _ in range(N)]
answer = 0
for i in arr:
    if target in i+i:
        answer += 1
print(answer)
