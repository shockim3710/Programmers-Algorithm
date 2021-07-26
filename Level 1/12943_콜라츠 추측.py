def solution(num):
    answer = 0

    # 500번을 반복하여
    # 1이 되기전까지 짝수홀수 규칙에 맞춰
    # num에 다시 저장하고 카운트
    # 만약 1이되면 break
    for i in range(500):
        if num == 1:
            break
        else:
            if num % 2 == 0:
                num = num / 2
            else:
                num = num * 3 + 1

            answer += 1

    # 500번을 반복해도 1이되지 않으면
    # -1을 출력
    if num != 1:
        answer = -1

    return answer