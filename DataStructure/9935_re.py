import sys
import re
input = sys.stdin.readline

def sol():
    string = input().strip()
    target = input().strip()

    slen = len(string)
    tlen = len(target)


    word = []

    for c in string:
        word.append(c)
        if tlen <= slen and "".join(word[len(word)-tlen:]) == target:
            for i in range(tlen):
                word.pop()

    if not word:
        print("FRULA")
    else:
        print("".join(word))






sol()
