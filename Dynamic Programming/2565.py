#2565 전깃줄
import sys


def solve(start):
    #start는 시작 좌표
    if dp[start] != -1:
        return dp[start]

    #기본 전기줄 개수
    base = 1
    tmpbox =[]
    for i in range(start+1,num):
        print("현재 애는 얩니다 [{} {}]".format(box[start][0], box[start][1]))

        if box[start][0] <= box[i][0] and box[start][1] <= box[i][1]:
            print("제가 뽑은 애는 얩니다 {} {}".format(box[i][0],box[i][1]))
            tmpbox.append((box[i][0],box[i][1]))

        elif box[start][0] >=box[i][0] and box[start][1] >= box[i][1]:
            print("제가 뽑은 애는 얩니다 {} {}".format(box[i][0],box[i][1]))
            tmpbox.append((box[i][0],box[i][1]))

        print(tmpbox)
    return dp[start]






num = int(input())
box=[]
dp  = [-1]*num

for _ in range(num):
    start,end =map(int,sys.stdin.readline().split())
    box.append((start,end))

solve(0)

print(dp)