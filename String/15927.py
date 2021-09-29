# 15927
import sys
input = sys.stdin.readline

def sol():
    def is_palindrome(sub_string):
        sub_length = len(sub_string)
        # 길이가 1이면 무조건 회문
        if sub_length == 1:
            return True

        # 짝수인 경우
        if not sub_length % 2:
            if sub_string[:sub_length//2] == sub_string[sub_length//2:][::-1]:
                return True
            return False

        # 홀수인 경우
        else:
            if sub_string[:(sub_length // 2)] == sub_string[(sub_length // 2)+1:][::-1]:
                return True
            return False


    string = input().strip()
    length = len(string)
    dp = [0] * length

    tmp_str = string[0]


    for i in range(1,length):

        if is_palindrome(tmp_str+string[i]):
            dp[i] = 0
            tmp_str = string[i]
        else:
            tmp_str += string[i]
            dp[i] = len(tmp_str)

    result = max(dp)
    print(result if result else -1)


sol()