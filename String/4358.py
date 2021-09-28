# 4358 not과 != 의 차이
from collections import defaultdict
import sys
input = sys.stdin.readline

def sol():
    trees = defaultdict(int)
    count = 0

    while 1:
        tree_name = input().strip()
        if not tree_name:
            break

        trees[tree_name] += 1
        count += 1

    for key in sorted(trees.keys()):
        print("{} {:.4f}".format(key,round((trees[key]/count)*100,4)))

sol()
