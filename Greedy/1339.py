#1339 단어수학

import sys

def sol():
    case = int(input())
    wordbox =[sys.stdin.readline().rstrip() for i in range(case)]
    assign_value = 9
    word_dic={}


    #예외적인 경우
    if len(wordbox)== 1:
        print(9)
        return ;

    # 긴 순서대로 도입
    wordbox.sort(key=lambda x:len(x),reverse=True)

    for i in range(len(wordbox)-1):
        first=len(wordbox[i])
        second=len(wordbox[i+1])

        common = min(first,second)

        # 자리수 다른 부분에 대한 처리 ( 같으면 지나침 )
        for c in range(first-second):
            if wordbox[i][c] not in word_dic:
                # 값 할당 후 하나 줄이기
                word_dic[wordbox[i][c]] = assign_value
                assign_value -= 1

        # 자리수 같은 부분에 대한 처리
        # ex) ABCDE SDF     first : 5 second 3: common 3  0~ 2까지는 처리 / first-second ~ common
        for c in range(first-second,first-second+common):
            if wordbox[i][c] not in word_dic:
                word_dic[wordbox[i][c]] = assign_value
                assign_value -= 1

            if wordbox[i+1][c-(first-second)] not in word_dic:
                word_dic[wordbox[i+1][c-(first-second)]] = assign_value
                assign_value -= 1

    print(word_dic)

    # 문자 -->  숫자
    result = 0
    for word in wordbox:
        # 원래 for 문 돌때 word가 바뀌는 것은 좋지 않지만, 여기서는 영향이 없기 때문에 괜찮아보인다.
        tmpresult = ""
        for w in word:
            tmpresult += str(word_dic[w])
        result += int(tmpresult)


    print(result)

sol()