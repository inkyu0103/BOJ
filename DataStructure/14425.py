#14425 문자열 집합(7시 49분 ~ 7시 53분)

import sys
input = sys.stdin.readline

N,M = map(int,input().split())
answer = 0
letter_set = set()
for _ in range(N):
    letter_set.add(input().strip())

for _ in range(M):
    target_letter = input().strip()
    if target_letter in letter_set:
        answer += 1

print(answer)

