def solution(array, commands):
    answer = []

    for i in range(len(commands)):
        cut = []

        for j in range(commands[i][0] - 1, commands[i][1]):
            cut.append(array[j])  # commands 범위까지 cut에 추가

        cut.sort()
        # cut에서 원하는 위치의 숫자를 answer에 추가
        answer.append(cut[commands[i][2] - 1])

    return answer