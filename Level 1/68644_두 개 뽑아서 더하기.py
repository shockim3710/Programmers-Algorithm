def solution(numbers):
    answer = set() # 집합으로 선언하여 중복숫자 제거

    # i번째 숫자와 i번째 숫자를 제외한 수를 더함
    # i번째 숫자를 제외한 수에는 i전의 수는 제외함
    for i in range(len(numbers)):
        for j in range(1, len(numbers)-i):
            answer.add(numbers[i]+numbers[j+i])

    answer = list(answer) # 집합을 리스트로 변환
    answer.sort() # 파이썬의 set은 순서를 보장하지 않는 해시셋이므로 다시 정렬

    return answer