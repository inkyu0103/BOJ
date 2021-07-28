# 9019 시작시간 1시 16분 / 첫 시도 1시 37분 (21분) --> 런타임 에러 / 2차 1시 46분 (런타임에러, 입력값이 0일때) : python3 시간초과 / pypy --> 오답.) / 3차 시도 --> zfill을 이용해서 고침. (2시 6분)

from collections import deque,defaultdict
import sys
input = sys.stdin.readline

'''
엄청 여러가지의 케이스가 존재
visit dictionary를 통해서 존재 여부를 확인해야겠다.
'''

def D(target):
    target *= 2
    if target >9999:
        target %= 10000
    return target

def S(target):
    if target == 0:
        target = 9999

    else:
        target -= 1

    return target


def L(target):
    target_str = str(target).zfill(4)
    target_str = target_str[1:] + target_str[0]
    target = int(target_str)
    return target

def R(target):
    target_str = str(target).zfill(4)
    target_str = target_str[-1] + target_str[:-1]
    target = int(target_str)
    return target

def BFS(start,end):
    q = deque([(start,"")])
    visit = dict()
    visit[start] = 1


    while q:
        target,command = q.popleft()

        if target == end:
            print(command)
            return

        # D 함수
        target_to_D = D(target)
        if target_to_D not in visit:
            new_command = command+"D"
            visit[target_to_D] = 1
            q.append((target_to_D,new_command))


        target_to_S = S(target)
        if target_to_S not in visit:
            new_command = command+"S"
            visit[target_to_S] = 1
            q.append((target_to_S,new_command))

        target_to_L = L(target)
        if target_to_L not in visit:
            new_command = command+"L"
            visit[target_to_L] = 1
            q.append((target_to_L,new_command))

        target_to_R = R(target)
        if target_to_R not in visit:
            new_command = command+"R"
            visit[target_to_R] = 1
            q.append((target_to_R,new_command))


if __name__=='__main__':
    tc = int(input())
    for  _ in range(tc):
        start,end = map(int,input().split())
        BFS(start,end)