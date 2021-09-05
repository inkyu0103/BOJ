# 7453 합이 0인 네 정수 (무슨 12초 씩이나 주시네...) 그럴만두... 합이 0인 쌍을 구하시오.
# dp가 섞여있나?
import sys
input = sys.stdin.readline
N = int(input())
idx = [0]*N
answer = 0
data = {"A":[],"B":[],"C":[],"D":[]}
for _ in range(N):
    a,b,c,d = map(int,input().split())
    data["A"].append(a)
    data["B"].append(b)
    data["C"].append(c)
    data["D"].append(d)

for i in data:
    data[i].sort()







