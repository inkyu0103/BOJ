from collections import defaultdict


def solution(commands):
    sheet = [[] for _ in range(50)]

    parent_node_mapper = defaultdict(list)

    def find_root(r, c):
        cur_r, cur_c = r, c

        while 1:
            p_r, p_c, val = sheet[cur_r][cur_c]

            if p_r == r and p_c == c:
                return [r, c]

            cur_r, cur_c = p_r, p_c

    def _update(*args):
        if len(args) == 2:
            value_1, value_2 = args
            for r in range(50):
                for c in range(50):
                    if sheet[r][c][2] == value_1:
                        sheet[r][c][2] = value_2

        else:
            r, c, value = args
            root_r, root_c = find_root(r, c)
            sheet[root_r][root_c] = value

    def _merge(r_1, c_1, r_2, c_2):
        # 같은 경우 무시
        if r_1 == r_2 and c_1 == c_2:
            return

        # 병합 대상 노드의 부모 찾기
        r_2, c_2 = find_root(r_2, c_2)

        # 병합 대상 노드의 모든 자식들에게 새로운 부모로 변경
        for r in range(50):
            for c in range(50):
                if sheet[r][c][0] == r_2 and sheet[r][c][0] == c_2:
                    sheet[r][c] = [r_1, c_1, sheet[r_1][c_1][2]]

    def _unmerge(t_r, t_c):
        # 해당 노드의 루트 좌표를 찾는다
        r_r, r_c = find_root(t_r, t_c)
        value = sheet[r_r][r_c][2]

        # 값을 초기화 한다.

        for r in range(50):
            for c in range(50):
                if sheet[r][c][0] == r_r and sheet[r][c][1] == r_c:
                    sheet[r][c] = [r, c, ""]

        # 값을 넣는다
        sheet[t_r][t_c] = [t_r, t_c, value]

    def _print(r, c):

        return

    for r in range(50):
        for c in range(50):
            sheet[r].append([r, c, ""])

    for command in commands:
        if command == "UPDATE":
            _update()

        if command == "MERGE":
            _merge()

        if command == "UNMERGE":
            _unmerge(r, c)

        if command == "PRINT":
            _print()


solution([])
