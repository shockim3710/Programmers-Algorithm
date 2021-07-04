def solution(n, lost, reserve):
    answer = n-len(lost)
    count = 0

    # 여벌이 있으면서 도난당한 학생은 pop하면서 answer에 +1
    for i in range(len(lost)):
        if lost[0+count] in reserve:
            reserve.pop(reserve.index(lost[0 + count]))
            lost.pop(0+count)
            answer += 1
        else:
            # pop을 하며 리스트 크기가 달라졌으므로 따로 count
            count += 1

    for j in range(len(lost)):
        # 여벌이 앞뒤에 있으면 answer에 +1하고 pop
        if lost[j]-1 in reserve:
            reserve.pop(reserve.index(lost[j]-1))
            answer += 1
        elif lost[j]+1 in reserve:
            reserve.pop(reserve.index(lost[j]+1))
            answer += 1

    return answer