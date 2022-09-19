# 2621
import sys
from collections import defaultdict
input = sys.stdin.readline


def rule_1(cards_mapper: dict):
    for key, value in cards_mapper.items():
        if len(value) == 5:
            sorted_value = sorted(value)

            for i in range(1, 5):
                if sorted_value[i] - sorted_value[i-1] != 1:
                    return 0

            return 900 + max(value)

    return 0


def rule_2(numbers_mapper: dict):
    # 같은 숫자는 색과 아무 상관이 없다.
    four_card_number = None

    for key, value in numbers_mapper.items():
        if len(value) == 4:
            return int(key) + 800

    return 0


def rule_3(numbers_mapper: dict):
    # 같은 숫자는 색과 아무 상관이 없다.
    triple_cards_number = None
    pair_cards_number = None

    for key, value in numbers_mapper.items():
        if len(value) == 3:
            triple_cards_number = key

        elif len(value) == 2:
            pair_cards_number = key

    if triple_cards_number and pair_cards_number:
        return int(triple_cards_number) + int(pair_cards_number) + 700

    return 0


def rule_4(cards_mapper: dict):
    for value in cards_mapper.values():
        if len(value) == 5:
            return 600 + max(value)

    return 0


def rule_5(number_list: dict):
    sorted_number_list = sorted(number_list)

    for i in range(1, 5):
        if sorted_number_list[i] - sorted_number_list[i - 1] != 1:
            return 0

    return sorted_number_list[-1] + 500


def rule_6(numbers_mapper: dict):
    # 3개의 숫자가 같아야 한다. -> 같은 수에 400 더하기
    for key, value in numbers_mapper.items():
        if len(value) == 3:
            return int(key) + 400
    return 0

def rule_7(numbers_mapper: dict):
    first_pair_number = None
    second_pair_number = None

    for key, value in numbers_mapper.items():
        if len(value) == 2:
            if first_pair_number is None:
                first_pair_number = int(key)
            else:
                second_pair_number = int(key)

    if first_pair_number is not None and second_pair_number is not None:
        return max(first_pair_number, second_pair_number) * 10 + min(first_pair_number, second_pair_number) + 300

    return 0


def rule_8(numbers_mapper: dict):
    for key, value in numbers_mapper.items():
        if len(value) == 2:
            return int(key) + 200


def rule_9(number_list: list):
    return 100 + max(number_list)


def sol():
    cards_mapper = defaultdict(list)
    numbers_mapper = defaultdict(list)
    number_list = []


    # save inputs
    for _ in range(5):
        card, number = input().rstrip().split(' ')
        cards_mapper[card].append(int(number))
        numbers_mapper[number].append(card)
        number_list.append(int(number))


    print(max([rule_1(cards_mapper),
        rule_2(numbers_mapper),
        rule_3(numbers_mapper),
        rule_4(cards_mapper),
        rule_5(number_list),
        rule_6(numbers_mapper),
        rule_7(numbers_mapper),
        rule_8(numbers_mapper),
        rule_9(number_list)]))

sol()
