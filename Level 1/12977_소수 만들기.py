from itertools import combinations # 조합을 만드는 라이브러리

def solution(nums):
    answer = 0

    for i in combinations(nums, 3): # 조합을 만드는 라이브러리 사용
        x = True # 소수인지 아닌지 판별

        for j in range(2,sum(i)//2): # 절반의 숫자로도 소수판별 가능
            # 소수가 아니라면 False 저장
            if sum(i)%j == 0:
                x = False
                break

        # True가 저장되어 있으면 소수이므로 1 카운트
        if x == True:
            answer += 1

    return answer