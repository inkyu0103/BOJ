# 2447 별찍기
def star(inp):
    if inp == 3 :
        return "*"


    return star(inp/3)





_input = int(input())

star(_input)


