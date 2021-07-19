def solution(left, right):
    num = [] # 약수의 개수를 저장
    answer = 0

    for i in range(left, right+1):
        count = 1 # 자기자신을 카운트한 약수의 개수

        for j in range(1, i//2+1):
            if i % j == 0:
                count += 1

        num.append(count)

    for i in range(len(num)):
        # 약수의 개수가 짝수이면 answer에 더함
        if num[i] % 2 == 0:
            answer += (left+i)
        else: # 홀수이면 answer에 뺌
            answer -= (left+i)

    return answer