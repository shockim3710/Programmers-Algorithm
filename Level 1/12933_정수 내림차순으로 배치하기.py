def solution(n):
    # 정수를 문자로 변환하고 내림차순으로 정렬하여
    # 리스트에 글자 하나하나를 한 문자로 합쳐서
    # 정수로 변환하여 answer에 저장
    answer = int(''.join(sorted((str(n)), reverse = True)))

    return answer

if __name__ == '__main__':
    print(solution(118372))