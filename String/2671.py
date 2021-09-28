# 2671
import re
import sys
input = sys.stdin.readline

def sol():
    target = input().strip()
    pattern = re.compile('(100+1+|01)+')

    print("SUBMARINE" if re.fullmatch(pattern,target) else "NOISE")

sol()