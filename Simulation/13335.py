# 13335
import sys

input = sys.stdin.readline

N, W, L = map(int, input().split())
trucks = list(map(int, input().split()))
bridge = [0] * W
answer = 0

while bridge:
    answer += 1
    bridge.pop(0)
    if trucks:
        if sum(bridge) + trucks[0] <= L:
            bridge.append(trucks.pop(0))
        else:
            bridge.append(0)
print(answer)
