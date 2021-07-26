def solution(x, n):
    answer = []

    # x가 0이면 n만큼 0추가
    if x == 0:
        answer = [0]*n
    # 0이아니면 절댓값으로 x부터 x*n까지
    # x만큼의 규칙을 가지고 answer에 추가
    else:
        for i in range(abs(x), abs(x * n) + 1, abs(x)):
            # x가 음수면 음수로 추가
            if x < 0:
                answer.append(-i)
            else:
                answer.append(i)

    return answer