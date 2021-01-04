#1319 단어수학 재도전

import sys
def sol():
    cnt = int(input())
    arr_alpha =[[0,chr(i)] for i in range(65,91)]
    word_box = []
    answer = 0
    count = 9

    for i in range(cnt):
        word = sys.stdin.readline().rstrip()
        word_box.append(word)
        for w in range(len(word)):
            arr_alpha[ord(word[w])-65][0] += 10**(len(word)-(w+1))

    # 값 기준으로 정렬
    arr_alpha.sort(reverse=True)
    # 값 할당
    for i in arr_alpha:
        if i[0] == 0 :
            return answer
        answer += i[0]*count
        count -= 1


    return answer

print(sol())