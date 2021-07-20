def solution(n, arr1, arr2):
    answer = []

    def digits(x): # n자릿수를 못채우면 0 추가하는 함수
        if len(x) < n:
            # 앞자리수부터 0을 채우기위해 뒤집음
            x = x[::-1]
            for j in range(n - len(x)):
                x += '0'

            x = x[::-1]

        return x

    for i in range(n):
        # 이진수로 변환후 앞에 0b를 제외하기위해 슬라이싱
        num1 = bin(arr1[i])[2:]
        num2 = bin(arr2[i])[2:]
        width = '' # #과 공백으로 변환한 가로줄 저장

        # n자릿수 채운 이진수를 저장
        num1Digits = digits(num1)
        num2Digits = digits(num2)

        # 둘다 0일때는 공백, 아니면 #을 추가
        for k in range(n):
            if num1Digits[k] == '0' and num2Digits[k] == '0':
                width += ' '
            else:
                width += '#'

        answer.append(width) # 변환된 가로줄을 answer에 추가

    return answer