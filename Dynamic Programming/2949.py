# 숫자 맞추기 12시 20분

'''
왼쪽으로 돌리면 ( 1작아짐 / 1인 경우에는 9로 변화 )다같이 돌아감

오른쪽으로 돌리면 그 나사만 돌아감

최소로 돌리는 경우는 우째야할까?
둘중에 하나다보니, 누구를 먼저 맞추는지를 기준으로 돌려봐야 할듯.

아니구나 N가지네 (10000개 이하)

쩝.. dp는 잠시패스..
다 dp네[
'''


import sys
input = sys.stdin.readline

N = int(input())
user_input = int(input())
target = int(input())

