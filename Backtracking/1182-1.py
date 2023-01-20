import sys

input = sys.stdin.readline

N, S = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
answer = 0
# print(N, S)


def func(k, total):
    global answer
    # 합이 S와 같은 경우 - 성공
    if k == N:
        if total == S:
            answer += 1
        return
    func(k + 1, total)
    func(k + 1, total + numbers[k])


func(0, 0)
print(answer if S != 0 else answer - 1)
