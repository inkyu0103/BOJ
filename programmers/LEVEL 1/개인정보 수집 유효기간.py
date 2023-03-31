def expire_date(validate_month, year, month, day):
    new_year, new_month, new_day = year, month + validate_month, day

    if new_month > 12:
        y, m = divmod(new_month, 12)
        new_year += y
        new_month = m

        if new_month == 0:
            new_year -= 1
            new_month = 12

    if new_day == 1:
        new_day = 28

        if new_month == 1:
            new_month = 12
            new_year -= 1

        else:
            new_month -= 1

    else:
        new_day -= 1

    print(new_year, new_month, new_day)
    return new_year, new_month, new_day


def solution(today, terms, privacies):
    today_year, today_month, today_day = map(int, today.split("."))
    term_dict = {}
    answer = []

    for term in terms:
        term_type, validate_period = term.split()
        term_dict[term_type] = int(validate_period)

    for idx, privacy in enumerate(privacies):
        s_date, term_type = privacy.split()
        s_year, s_month, s_day = map(int, s_date.split("."))

        e_year, e_month, e_day = expire_date(
            term_dict[term_type], s_year, s_month, s_day
        )

        # 연도
        if e_year < today_year:
            answer.append(idx + 1)
            continue

        if e_year == today_year:
            if e_month < today_month:
                answer.append(idx + 1)

            elif e_month == today_month:
                if e_day < today_day:
                    answer.append(idx + 1)

    return answer
