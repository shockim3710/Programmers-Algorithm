def solution(N, stages):
    answer = []
    fail = dict()
    num = len(stages) # 총 도전한 사용자

    for i in range(1, N+1):
        # 실패한 사람이 없으면 그 스테이지에 0 저장
        if i not in stages:
            fail[i] = 0
        # 스테이지에 실패율을 저장하고
        # 도전한 사용자에서 실패한 사용자 빼기
        else:
            fail[i] = stages.count(i)/num
            num -= stages.count(i)

    # 람다식을 이용하여 value값으로 내림차순 정렬
    failSort = sorted(fail.items(), key=lambda x: x[1], reverse=True)

    # 정렬된 key값을 answer에 추가
    for i in range(N):
        answer.append(failSort[i][0])

    return answer