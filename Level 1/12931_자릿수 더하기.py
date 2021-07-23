def solution(n):
    answer = 0

    # n을 문자로 변환하여 숫자 하나하나를
    # answer에 숫자로 더함
    for i in range(len(str(n))):
        answer += int(str(n)[i])

    return answer