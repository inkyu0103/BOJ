#1963
import sys
from collections import deque
input = sys.stdin.readline

'''
제한된 범위에서 소수를 판단하면 되니까 크게 문제되지 않을 듯 싶다.

어느 자리를 움직일 것인지?
1의 자리, 10의 자리, 100의 자리, 1000의 자리

visit에 있는지 확인해서 추가해야 한다.

'''

def sol():
    # 에라토스 테네스의 체 만드는 곳
    def eratos():
        prime = set(i for i in range(2, 10000))
        result = set()

        for i in range(2, 10000):
            j = 2
            while i * j < 10000:
                if i * j in prime:
                    prime.remove(i * j)
                j += 1

        for i in prime:
            if i > 1000:
                result.add(i)

        return result

    # 소수 경로의 타겟이 되는 곳을 return
    def move_num(target):
        result = set()

        for idx in range(4):
            for i in range(0, 10):
                move_target = list(str(target))
                move_target[idx] = str(i)

                value = int("".join(move_target))

                if isPrime(value):
                    result.add(value)
        return result


    def isPrime(target):
        return True if target in prime else False

    ######################################################################

    prime = eratos()
    tc = int(input())
    for _ in range(tc):

        # start, end input
        s,e = map(int,input().split())
        if s == e:
            print(0)
            continue

        visit = set()
        q = deque([[0,s]])
        visit.add(s)

        flag = 0
        while q:
            c,node = q.popleft()
            for nnode in move_num(node):
                if nnode == e:
                    print(c+1)
                    flag = 1
                    break

                if nnode not in visit:
                    q.append([c+1,nnode])
                    visit.add(nnode)

            if flag:
                break

        if not flag:
            print('Impossible')

sol()