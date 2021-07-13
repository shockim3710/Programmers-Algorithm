def solution(d, budget):
    money = 0 # 구매한 비용
    answer = 0

    # 최대한 많은 부서를 선택하기 위해
    # 적은 돈의 부서대로 정렬
    d.sort()

    for i in d:
        money += i

        if money > budget: # 구매한 비용이 예산을 초과하면 break
            break
        else: # 초과하지 않으면 1씩 더함
            answer += 1

    return answer

print(solution([2,2,3,3], 10))