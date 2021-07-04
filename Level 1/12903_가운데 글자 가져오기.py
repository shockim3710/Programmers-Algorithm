def solution(s):
    if len(s)%2 == 0: # 글자가 짝수개이면 가운데 2글자를 출력
        answer = s[len(s)//2 - 1]+s[len(s)//2]
    else: # 글자가 홀수개이면 가운데 글자를 출력
        answer = s[len(s)//2]

    return answer