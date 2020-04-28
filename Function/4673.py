#4673 self num

def self_num (_in):
    result  =_in
    for i in str(_in):
        result += int(i)

    return result

box = list(range(1,10001))
temp_box =list(range(1,10001))

for i in box :
    if self_num(i) in temp_box:
        temp_box.remove(self_num(i))


for i in temp_box:
    print(i)

