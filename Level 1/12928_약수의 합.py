def solution(n):
    answer = n # 자기자신은 미리 더함

    # n의 반만 확인해도 약수가 나오므로
    # 약수일 때 answer에 더함
    for i in range(1, (n//2)+1):
        if n % i == 0:
            answer += i

    return answer