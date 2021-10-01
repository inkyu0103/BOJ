# 17609
import sys
input = sys.stdin.readline

def sol():

    def isPalin(target):
        length = len(target)
        # 홀수 문자일 경우
        if length % 2 and target[:length//2] == target[(length//2)+1:][::-1]:
            return True

        # 짝수 문자일 경우
        elif not length%2 and target[:length//2] == target[length//2:][::-1]:
            return True

        else:
            return False

    def isLikePalin(target):

        length = len(target)
        # 홀수 문자일 경우
        if length % 2 and target[:length // 2] == target[(length // 2) + 1:][::-1]:
            return True

        # 짝수 문자일 경우
        elif not length % 2 and target[:length // 2] == target[length // 2:][::-1]:
            return True

        else:
            return False


    tc = int(input())
    words = [input().strip() for _ in range(tc)]

    for word in words:
        if isPalin(word):
            print(0)
            continue

        flag = 0
        for i in range(len(word)):
            target = ''

            for j in range(len(word)):
                if i != j:
                    target += word[j]

            if isLikePalin(target):
                flag = 1
                print(1)
                break

        if not flag:
            print(2)
sol()