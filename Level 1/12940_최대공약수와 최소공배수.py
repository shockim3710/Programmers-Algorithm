def solution(n, m):
    maxYak = 1 # 최대공약수
    minBae = 1 # 최소공배수
    answer = []

    while True:
        # 안나누어 떨어질때를 확인
        check = False

        for i in range(2, min(n, m)+1):
            # 하나의 수가 n,m에 나누어떨어지면
            # 최대공약수에 곱하고
            # n,m을 그 수로 나누어 저장하고 break
            if n % i == 0 and m % i == 0:
                maxYak *= i
                n = n // i
                m = m // i
                check = True

                break

        # 더이상 나누어 떨어지지않으면
        # 최th공배수에 최대공약수,n,m을 곱하고
        # answer에 최대공약수, 최소공배수 추가하고 break
        if check == False:
            minBae *= (maxYak * n * m)

            answer.append(maxYak)
            answer.append(minBae)
            break

    return answer