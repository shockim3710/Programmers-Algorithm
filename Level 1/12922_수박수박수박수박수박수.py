def solution(n):
    answer = ''

    for i in range(1, n+1):
        if i % 2 != 0: # i가 짝수이면 '수'
            answer += '수'
        else: # 홀수이면 '박'
            answer += '박'

    return answer