# 1662 압축

def sol(string,length,init_idx):
    stack = []
    for i in range(init_idx,length):
        if string[i] == "(":
            tmpString, startIdx = sol(string,length,init_idx+i+1)
            stack.append(stack.pop()*tmpString)
            break
        elif string[i] == ")":
            return ("".join(stack),init_idx+i+1)

        else:
            stack.append(string[i])








    return



if __name__ == "__main__" :
    user_input = input()
    sol(user_input,len(user_input),0)
