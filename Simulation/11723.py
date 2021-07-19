# 집합

'''
add x
remove x
check x
toggle x
all
empty
'''

import sys
input = sys.stdin.readline

def add(target):
    S.add(target)

def remove(target):
    if target not in S:
        return
    S.remove(target)

def toggle(target):
    if target in S:
        remove(target)
    else:
        add(target)

def check(target):
    if target in S:
        print(1)
    else:
        print(0)

def all():
    global S
    S = set(i for i in range(1,21))

def empty():
    global S
    S =set()




if __name__ =="__main__":
    M = int(input())
    S = set()
    for _ in range(M):
        target_list = input().strip().split(" ")

        if len(target_list)==2:
            command, num = target_list
            if command == "add":
                add(num)
            elif command == "remove":
                remove(num)

            elif command == "toggle":
                toggle(num)
            elif command == "check":
                check(num)

        else:
            command = target_list[0]
            if command == "all":
                all()
            else:
                empty()
