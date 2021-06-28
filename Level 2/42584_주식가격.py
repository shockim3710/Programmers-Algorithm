def solution(prices):
    answer = []

    for i in range(len(prices)): # i초 시점
        count = 0

        for j in range(1, len(prices) - i):
            num = prices[i] # i초 시점을 num으로 지정
            # prices의 j+i부터 끝까지 num과 비교해서
            # 크거나 같으면 count 1 증가, 작으면 break
            if num <= prices[j + i]:
                count += 1
            else:
                count += 1
                break

        answer.append(count) # count한 값을 answer에 추가

    return answer