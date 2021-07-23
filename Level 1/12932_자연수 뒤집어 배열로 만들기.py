def solution(n):
    answer = []

    # 자연수 n을 문자로 변환하여
    # 맨 뒷자리부터 answer에 숫자로 추가
    for i in range(1, len(str(n))):
        answer.append(int(str(n)[-i]))
    
    # n의 첫번째 숫자는 따로추가
    answer.append(int(str(n)[0]))

    return answer