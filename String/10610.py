from itertools import permutations
import sys
input = sys.stdin.readline

def sol():
    n = list(input().strip())
    n.sort(reverse=True)
    target = 0


    for c in n:
        target += int(c)

    if n[-1] != '0' or target%3:
        print(-1)
        return;

    else:
        print("".join(n))


sol()




'''length = len(n)
candidate = []

for r in range(2,length+1):
    for target in permutations(n,r):
        val = int("".join(list(target)))
        if not val%30:
            candidate.append(val)
print(max(candidate) if candidate else -1)
'''



