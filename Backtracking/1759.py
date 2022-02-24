# 1759 아하 오름차순 순서로 되어있나보구나?
# 최소 한 개의 모음과 최소 두개의 자음으로 구성되어있어야 한다.
# 이 조건 만족시키려면... 백트래킹 할 때, 개수를 붙여서 넣어주어야 할 거 같다.
# 그리고 출발 지점을 넘겨주면서, 항상 오름차순으로 선택 할 수 있도록 하자

import sys
input = sys.stdin.readline

def sol():
    L,C = map(int,input().split())
    char_arr = sorted(input().strip().split())
    length = len(char_arr)
    consonants = {'a', 'e', 'i', 'o', 'u'}
    answers = []
    visit = [0]*length


    def dfs(start,depth,consonant,vowel,word):
        # 정확한 경우
        if depth == L and consonant and vowel>=2:
            return answers.append(word)

        for x in range(start,C):
            if not visit[x]:
                visit[x] = 1

                if char_arr[x] in consonants:
                    dfs(x+1,depth+1,consonant+1,vowel,word+char_arr[x])

                else:
                    dfs(x+1,depth+1,consonant,vowel+1,word+char_arr[x])

                visit[x] = 0

    dfs(0,0,0,0,'')

    for answer in answers:
        print(answer)
sol()