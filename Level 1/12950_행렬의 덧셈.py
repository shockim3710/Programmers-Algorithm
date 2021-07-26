def solution(arr1, arr2):
    # 이중리스트를 arr1[0], arr1 길이만큼 미리 추가
    answer = [[0]*len(arr1[0]) for _ in range(len(arr1))]

    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            answer[i][j] = arr1[i][j]+arr2[i][j]

    return answer