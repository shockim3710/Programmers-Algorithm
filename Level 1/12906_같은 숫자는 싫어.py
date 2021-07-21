def solution(arr):
    answer = []

    for i in range(len(arr) - 1):
        # 연속적인 숫자가 같지 않으면 answer에 그 숫자를 저장
        if arr[i] != arr[i + 1]:
            answer.append(arr[i])

    # 마지막 숫자는 중복되지 않아도 추가되지 않으므로
    # 따로 answer에 추가
    answer.append(arr[-1])

    return answer