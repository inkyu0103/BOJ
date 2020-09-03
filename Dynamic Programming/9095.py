#9095

def solve (_input) :
    global count
    if _input == 0:
        count += 1
        return

    elif _input < 0:
        return

    else:
        solve(_input-1)
        solve(_input-2)
        solve(_input-3)


tc = int(input())
for i in range(tc):
    target = int(input())
    count = 0
    solve(target)
    print(count)


