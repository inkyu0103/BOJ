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

        for idx, price in enumerate(prices):
            if max_index == idx:
                max_price = max(prices[idx+1:])
                max_index = prices[idx+1:].index(max_price)
                print('new prices', max_price,max_index)

            else:
                print('new prices', max_price, max_index)
                if price < max_price:
                    profit += max_price-price

        print(profit)

sol()
