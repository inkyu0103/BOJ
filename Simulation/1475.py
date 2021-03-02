# 1475 방 번호

def sol():
    data = [0]*9
    _input = input()

    for i in _input:
        if int(i) == 9:
            data[6] += 1
        else:
            data[int(i)] += 1

    if data[6] % 2 == 0 :
        data[6] /=2
    else:
        data[6] = data[6]//2 + 1


    print(int(max(data)))
sol()
