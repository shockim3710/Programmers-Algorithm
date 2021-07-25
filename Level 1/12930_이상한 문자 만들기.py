def solution(s):
    answer = ''
    count = 1

    for i in s:
        # 문자가 알파벳이고
        # 0번째부터 대문자이므로 1부터 count를 하여
        # 홀수번째면 대문자 짝수번째면 소문자로
        # 규칙을 변경하여 answer에 추가
        if i.isalpha() == True:
            if count % 2 != 0:
                answer += i.upper()
            else:
                answer += i.lower()
            count += 1
        # 알파벳이 아니면 공백이므로
        # 공백을 answer에 추가하고 count 초기화
        else:
            answer += i
            count = 1

    return answer