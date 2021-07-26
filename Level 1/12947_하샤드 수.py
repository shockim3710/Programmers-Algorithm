def solution(x):
    num = 0

    # x를 문자로 변환하여
    # num에 한글자씩 숫자로 더함
    for i in str(x):
        num += int(i)

    # 더한값이 x에 나누어떨어지면 True
    # 아니면 False 출력
    if x % num == 0:
        answer = True
    else:
        answer = False

    return answer