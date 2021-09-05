import re
import sys
input = sys.stdin.readline

tc= int(input())
for _ in range(tc):
    user = input().strip()
    result = re.fullmatch("(100+1+|01)+",user)

    if not result:
        print("NO")
    else:
        print("YES")