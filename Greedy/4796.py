# 4796 캠핑
import sys
'''
 8일중 5일만 사용가능, 근데 20일 휴가임.
 최대한 많이 사용하는 것이 목표
 P일중 L일동안만 사용할 수 있는데, V일짜리 휴가 시작
 
 V // P 를 하면 휴가동안 운영하는 캠핑장의 사이클
 
 이런경우는 어떻게 하지? 
 XXXOOOOO/OOOOOXXX/OOOO
 
'''


def sol():
    count = 1

    while(1):
        answer = 0
        L, P, V = map(int,sys.stdin.readline().split())
        if L ==0 and P == 0 and V == 0 :
            return;

        # 한 사이클에서 이용할 수 있는 만큼 더하기
        for i in range(V//P):
            answer += L

        # V - (V//P)*P 남은 휴가 일 수
        if V - (V//P)*P >= L:
            answer += L

        else:
            answer += V-(V//P)*P

        print("Case {}: {}".format(count,answer))
        count +=1

sol()