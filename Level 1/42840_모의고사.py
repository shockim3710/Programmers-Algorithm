def solution(answers):
    people1 = [1, 2, 3, 4, 5]
    people2 = [2, 1, 2, 3, 2, 4, 2, 5]
    people3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    count1 = 0
    count2 = 0
    count3 = 0

    answer = []

    for i in range(len(answers)):
        # 반복되는 찍은 정답마다 잘라서
        # answers와 비교하여 카운트
        if answers[i] == people1[i%5]:
            count1 += 1
        if answers[i] == people2[i%8]:
            count2 += 1
        if answers[i] == people3[i%10]:
            count3 += 1

    # 많이 맞춘 사람과 동점이 있는지 비교
    if max(count1, count2, count3) == count1:
        answer.append(1)
    if max(count1, count2, count3) == count2:
        answer.append(2)
    if max(count1, count2, count3) == count3:
        answer.append(3)

    return answer