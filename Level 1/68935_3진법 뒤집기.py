def solution(n):
    div = n # 자연수를 나눈 몫
    ternary = '' # 앞뒤반전한 3진법
    answer = 0

    if n == 1: # 자연수가 1일때는 3진법 1로 저장
        ternary = '1'
    else:
        while True:
            # 3진법으로 바꾸는 마지막 몫, 나머지
            if div // 3 == 0 or div // 3 == 1 or div // 3 == 2:
                ternary += str(div % 3) + str(div // 3)
                break
            # 3진법으로 바꾸는 몫, 나머지를 문자로 저장
            else:
                ternary += str(div % 3)
                div = div // 3

    count = len(ternary)-1 # 3의 지수승을 저장

    for i in ternary:
        answer += int(i) * (3**count)
        count -= 1 # 3의 지수승을 1씩 빼서 저장

    return answer