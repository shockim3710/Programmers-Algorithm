def solution(n):
    answer = 1

    # 2를 제외한 짝수는 전부 소수가 안되므로
    # 2는 카운트를 하고 2가 아닐때만 소수판별
    if n != 2:
        for i in range(3, n+1, 2):
            sosu = True
            # 3부터 n까지 홀수번째에서
            # 2부터 제곱근까지 나누어 떨어지는수가 있으면
            # break 걸고 False 처리
            for j in range(2, int((i**0.5))+1):
                if i % j == 0:
                    sosu = False
                    break
            # 나누어 떨어지는수가 없었으면
            # answer에 1더함
            if sosu == True:
                answer += 1

    return answer