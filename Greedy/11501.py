# 11501

import sys
input = sys.stdin.readline

def sol():
    tc = int(input())
    for _ in range(tc):
        days = int(input())
        prices = list(map(int, input().split()))
        profit = 0

        max_price = max(prices)
        max_index = prices.index(max_price)

        for idx in range(len(prices)-1):
            # 자신이 max값인 경우 -> max_value / idx 재설정
            if max_index == idx:
                max_price = max(prices[idx+1:])
                max_index = prices[idx+1:].index(max_price)+(idx+1)
                continue

            # 그렇지 않은 경우 -> 이익 계산
            if max_price > prices[idx]:
                profit += max_price - prices[idx]

        print(profit)


def sol1():
    tc = int(input())
    for _ in range(tc):
        days = int(input())
        prices = list(map(int, input().split()))
        profit = 0

        max_price = prices[-1]

        for i in range(len(prices)-1, -1, -1):
            if max_price >= prices[i]:
                profit += max_price - prices[i]

            else:
                max_price = prices[i]

        print(profit)


sol1()
