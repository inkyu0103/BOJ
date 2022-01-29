# 9037 The candy war
'''
요구사항
1. 모든 아이들이 가지고 있는 사탕 개수가 배열로 주어진다. -> 초기에 주어질 때 짝수로 맞춰줄 것
-  base case
- 한 사람만 있는가 ?
- 모두 같은 개수를 가지고 있는가?
-> return 0
---
2. 자신이 가지고 있는 사탕의 절반을 오른쪽 아이에게 준다.

3. 사탕을 홀수개 가지고 있으면 선생님이 한 개씩 더 준다.

4. 순환수 +1 , 모두 같은 개수를 가지는지 확인
---
'''

import sys
input = sys.stdin.readline

def share_half_candy(candy_info:list):
    # need batch update
    new_candy_info = [candy for candy in candy_info]
    length = len(candy_info)

    for idx,candy_num in enumerate(candy_info):
        new_candy_info[idx%length] -= candy_num//2
        new_candy_info[(idx+1)%length] += candy_num//2

    return new_candy_info


def make_candy_even (candy_info:list):
    new_candy_info =[]
    for candy_num in candy_info:
        if not candy_num%2:
            new_candy_info.append(candy_num)
            continue
        new_candy_info.append(candy_num+1)
    return new_candy_info

def is_equal_candy (candy_info:list):
    temp_candy = candy_info[0]
    for candy_num in candy_info:
        if temp_candy != candy_num:
            return False
    return True

def sol():
    tc = int(input())
    for _ in range(tc):
        circulate = 0
        num_of_children = int(input())
        candy_info = list(map(int,input().split())) # 계속 mutate 되어도 상관 없는가?

        candy_info = make_candy_even(candy_info)

        # base case
        if num_of_children == 1 or is_equal_candy(candy_info):
            print(circulate)
            continue

        while True:
            candy_info = share_half_candy(candy_info)
            candy_info = make_candy_even(candy_info)

            if is_equal_candy(candy_info):
                print(circulate+1)
                break

            circulate += 1
sol()
