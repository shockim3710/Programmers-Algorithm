def solution(nums):
    choice = len(nums) // 2
    nums = set(nums) # 중복 제거를 위해 집합으로 변환

    # 선택하는 마리보다 중복없는 폰켓몬이 적으면
    # 폰켓몬의 마리수를 출력
    if len(nums) < choice:
        answer = len(nums)
    # 그렇지 않으면 선택하는 마리수를 출력
    else:
        answer = choice

    return answer