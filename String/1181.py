import sys
input = sys.stdin.readline

def sol():
    N = int(input())
    # convert list to set time complexity : O(n) vice versa
    words = list(set(input().strip() for _ in range(N)))
    words.sort(key=lambda x:(len(x),x))

    #"\n".join(word) 도 괜찮다...!
    for word in words:
        print(word)

sol()