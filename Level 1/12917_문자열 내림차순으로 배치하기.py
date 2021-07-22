def solution(s):
    answer = ''

    # 문자를 내림차순으로 리스트에 저장
    arr = sorted(s, reverse=True)

    # 리스트에 있는 문자를 합쳐서 answer에 저장
    for i in arr:
        answer += i

    return answer