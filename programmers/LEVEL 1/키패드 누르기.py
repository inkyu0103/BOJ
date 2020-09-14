def solution(numbers, hand):
    key = {1: (0, 0), 2: (0, 1), 3: (0, 2),
           4: (1, 0), 5: (1, 1), 6: (1, 2),
           7: (2, 0), 8: (2, 1), 9: (2, 2),
           "*": (3, 0), 0: (3, 1), "#": (3, 2)}

    left = [1, 4, 7]
    right = [3, 6, 9]
    last_left = ["*"]
    last_right = ["#"]
    answer = ''

    for num in numbers:
        if num in left:
            answer += "L"
            last_left.append(num)
        elif num in right:
            answer += "R"
            last_right.append(num)
        else:
            left_dist = abs(key[last_left[-1]][0] - key[num][0]) + abs(key[last_left[-1]][1] - key[num][1])
            right_dist = abs(key[last_right[-1]][0] - key[num][0]) + abs(key[last_right[-1]][1] - key[num][1])

            if left_dist == right_dist:
                if hand == "right":
                    answer += "R"
                    last_right.append(num)
                else:
                    answer += "L"
                    last_left.append(num)

            elif left_dist < right_dist:
                answer += "L"
                last_left.append(num)

            elif left_dist > right_dist:
                answer += "R"
                last_right.append(num)

    return answer