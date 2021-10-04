# 17609
import sys
input = sys.stdin.readline

def sol():
    # 투 포인터를 이용
    def isPalin(l,r):
        while l<r:

            if word[l] != word[r]:
                return False

            l+=1
            r-=1
        return True


    def isLikePalin(l,r,count):
        while l<r:
            if word[l] == word[r]:
                l+=1
                r-=1
                continue


            elif word[l] != word[r]:
                if not count :
                    val1 = isLikePalin(l+1,r,1)
                    val2 = isLikePalin(l,r-1,1)
                    if val1 or val2:
                        return True

                    else:
                        return False
                #  count
                else:
                  return False

        return True




    tc = int(input())

    for _ in range(tc):
        word = input().strip()
        word_length = len(word)

        if isPalin(0,word_length-1):

            print(0)
            continue

        if isLikePalin(0,word_length-1,0):
            print(1)
            continue

        print(2)

sol()