def solution(strings, n):
    # 같은 문자가 있을경우
    # 사전순으로 저장하기위해 정렬
    stringsSort = sorted(strings)
    # 중복 문자 제거하기위해
    # 집합으로 선언
    stringsDic = set()
    answer = []

    # n번째 문자 저장
    for i in stringsSort:
        stringsDic.add(i[n])

    # 중복 제거 후 리스트로 선언
    stringsDic = list(stringsDic)

    # n번째 문자가 리스트 안의 n번째 문자와 같으면
    # answer에 추가
    for j in range(len(stringsDic)):
        for k in range(len(strings)):
            # n번째 문자 오름차순 정렬
            if sorted(stringsDic)[j] == stringsSort[k][n]:
                answer.append(stringsSort[k])

    return answer


'''
# 다른 풀이
def solution(strings, n):
    answer = []

    # 문자열 앞에 n번째 문자를 추가하여 저장
    for i in range(len(strings)):
       strings[i] = strings[i].rjust(len(strings[i])+1, strings[i][n])

    # 수정된 리스트를 정렬하고
    # 추가한 n번째 문자를 슬라이싱하여
    # answer에 추가
    for i in sorted(strings):
        answer.append(i[1::])

    return answer
'''