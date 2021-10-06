# 2866
import sys
input = sys.stdin.readline

def sol():
    R,C = map(int,input().split())
    words = []
    visited = set()

    for _ in range(R):
        words.append(list(input().rstrip()))

    def overlap(start):

        for c in range(C):
            check_word = ''
            for r in range(start, R):
                check_word += words[r][c]

            if check_word in visited:
                return True

            else:
                visited.add(check_word)
        return False

    l,r = 0, R-1

    result = -1

    while l<=r:
        mid = (l+r) // 2

        if overlap(mid):
            r = mid-1

        else:
            l = mid + 1
            result = mid

    print(result)
sol()