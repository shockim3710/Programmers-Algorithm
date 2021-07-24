def solution(n):
    answer = 0

    # n의 루트를 씌운 값은 나누어 떨어져도 뒤에 .0이 붙으므로
    # 그 값을 모듈러 1했을 때 0인지 아닌지 판별
    # 나누어 떨어지면 0, 아니면 루트씌운값
    if (n**0.5) % 1 == 0:
        answer = (n**0.5 + 1) ** 2
    else:
        answer = -1

    return answer