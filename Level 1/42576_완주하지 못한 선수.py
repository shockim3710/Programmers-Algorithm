def solution(participant, completion):
    answer = ''

    # 참여선수와 완주선수를 정렬
    participant.sort()
    completion.sort()

    for i in range(len(participant)):
        # 만약 참여선수와 완주선수가 같지않으면 정답에 저장하고 break
        if participant[i] != completion[i]:
            answer = participant[i]
            break
        else:
            # 만약 완주선수 배열이 비어있으면
            # 남아있는 참여선수를 정답에 저장하고 break
            if len(completion) == 0:
                answer = participant[0]
                break

    return answer