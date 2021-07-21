def solution(s):
    answer = 0
    s = s[::-1] # 자릿수별로 추가하기위해 문자를 뒤집음

    for i in range(len(s)):
        # 문자가 숫자이면 자릿수만큼 곱해서 answer에 추가
        if s[i].isdigit() == True:
            answer += int(s[i])*(10**i)
        # 아니면 부호이므로 부로를 붙여 저장
        else:
            if s[i] == '+':
                answer = +answer
            if s[i] == '-':
                answer = -answer

    return answer

'''
# 다른 풀이
def solution(s):
    answer = int(s)
    return answer
'''