def solution(arr, divisor):
    answer = []

    # arr 안의 숫자가 divisor에 나누어 떨어지면
    # answer에 추가
    for i in arr:
        if i % divisor == 0:
            answer.append(i)

    # answer 리스트가 비어있으면 -1추가
    if len(answer) == 0:
        answer.append(-1)
    # 아니면 오름차순으로 정렬
    else:
        answer.sort()

    return answer