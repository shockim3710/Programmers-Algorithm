def solution(lottos, win_nums):
    count0 = 0 # 알아볼수 없는 번호 개수
    countWin = 0 # 당첨번호와 일치한 개수
    answer = []

    for i in range(len(lottos)):
        if lottos[i] == 0:
            count0 += 1
        elif lottos[i] in win_nums:
            countWin += 1

    # 당첨된 번호,알아볼수 없는 번호 없으면 최고순위 6등으로 저장
    if countWin == 0 and count0 == 0:
        answer.append(6)
    else:
        # 알아볼수 없는 번호가 남아있는 당첨번호보다 많으면
        # 남아있는 당첨번호 개수를 사용하여 최고순위를 저장
        if len(win_nums) - countWin < count0:
            answer.append(6 - (len(win_nums) - countWin) + 1)
        # 같거나 적으면 알아볼수 없는 번호가 전부 당첨번호라 가정,
        # 당첨번호와 알아볼수 없는 번호 개수를 사용하여 최고순위를 저장
        else:
            answer.append(6 - (countWin + count0) + 1)

    # 당첨된 번호가 없으면 최저순위 6등으로 저장
    if countWin == 0:
        answer.append(6)
    # 있으면 당첨번호 개수를 사용하여 최저순위를 저장
    else:
        answer.append(6 - countWin + 1)

    return answer