# 7785 회사에 있는 사람 (오후 7:36 ~ 7:40)
'''
로그가 주어졌을 때, 현재 회사에 있는 사람을 구하시오
set or dict로 풀면 될듯?
'''
import sys
input = sys.stdin.readline

tc = int(input())
people = set()

for _ in range(tc):
    name,state = input().strip().split(" ")
    if state == 'enter':
        people.add(name)
    else:
        people.remove(name)

answer = list(people)
answer.sort(reverse=True)

for i in answer:
    print(i)

