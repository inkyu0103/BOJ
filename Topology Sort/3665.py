# 3665 최종 순위

import sys

testCase = int(input())

for i in range(testCase):
    teamNum = int(sys.stdin.readline())
    beforeRank = list(map(int,sys.stdin.readline().split()))
    changeRankNum = int(input())

    for j in range(changeRankNum):
        a,b = map(int,sys.stdin.readline().split())
