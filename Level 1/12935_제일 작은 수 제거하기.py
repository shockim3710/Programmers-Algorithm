def solution(arr):
    answer = []

    # arr 길이가 1이면 answer에 -1추가
    if len(arr) == 1:
        answer.append(-1)
    # 아니면 arr에서 최솟값을 pop하여 answer에 추가
    else:
        arr.pop(arr.index(min(arr)))
        answer = arr

    return answer