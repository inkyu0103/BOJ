def solution(info, query):
    user_info = {}
    user_length = len(info)
    query_length = len(query)
    answer = []

    # 유저 분석
    for i in range(0, user_length):
        user_info[i] = info[i].split(" ")
    # 쿼리문 분석
    for q in query:
        tmp = 0
        query_detail = q.split(" and ")
        tmp_q = query_detail.pop()
        query_detail.extend(tmp_q.split(" "))

        l, d, c, s, g = query_detail

        for u in user_info:
            u_l, u_d, u_c, u_s, u_g = user_info[u]

            if l != "-" and l != u_l:
                continue

            if d != "-" and d != u_d:
                continue

            if c != "-" and c != u_c:
                continue

            if s != "-" and s != u_s:
                continue

            if int(g) <= int(u_g):
                tmp += 1

        answer.append(tmp)

    return answer