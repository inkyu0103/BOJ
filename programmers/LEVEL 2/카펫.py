# 카펫
def solution(brown, yellow):
    total = brown + yellow

    for width in range(1, yellow + 1):
        height, mod = divmod(yellow, width)
        height += 2
        width += 2

        height = min(height, width)
        width = max(height, width)

        if not mod and height * width == total:
            return [width, height]

