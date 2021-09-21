#1969 DNA
import sys
from collections import Counter
input = sys.stdin.readline

# O(MN)
def sol():
    N,M = map(int,input().split())
    DNA = [input().strip() for _ in range(N)]
    answer = ''
    dist = 0
    for m in range(M):
        tmp = ''
        for n in range(N):
            tmp += DNA[n][m]
        count = list(Counter(tmp).items())
        count.sort(key=lambda x:(-x[1],x[0]))
        target_str = count[0][0]
        answer += target_str

        for i in count:
            if i[0] != target_str:
                dist += i[1]

    print(answer)
    print(dist)







sol()