# 2800 괄호제거

def sol(string,start,end):
    stack = []
    for i in range(len(string)):
        if string[i] == "(":
            stack.append(i)
        elif string[i] == ")":
            sol(const_string,stack.pop(),i)






sol()

if __name__=="__main__":
    const_string = input()
    answer = []
    sol()