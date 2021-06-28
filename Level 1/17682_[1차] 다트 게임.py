def solution(dartResult):
    dartResult = list(dartResult) # 각각의 글자를 리스트로 저장
    num = [[] * 3 for i in range(3)] # num = [[], [], []]
    answer = 0
    nowNum = '0' # 10을 받기위해 문자가 오기전까지 string으로 합침
    count = 0 # 다트의 횟수

    for i in dartResult:
        if i.isdigit() == True: # i가 숫자라면
            if nowNum == '0':
                count += 1 # 10일때 중복으로 카운트하는것을 방지
            nowNum += i # 숫자를 nowNum으로 합쳐서 저장
        else:
            nowNum = int(nowNum) # string을 int로 변환

            if i.isalpha() == True or i == '#': # i가 문자거나 #이면
                if i == 'S':
                    nowNum **= 1 # nowNum의 1승
                elif i == 'D':
                    nowNum **= 2 # nowNum의 2승
                elif i == 'T':
                    nowNum **= 3 # nowNum의 3승
                elif i == '#':
                    nowNum = -1

                num[count-1].append(nowNum) # 각각의 리스트에 점수와 아차상 추가
            else: # i가 *이면
                if count == 3: # 3번째 기회이면 2번째 3번째에만 스타상 추가
                    num[1].append(2)
                    num[2].append(2)
                else:
                    for j in range(count):
                        num[j].append(2)

            nowNum = '0' # 점수 초기화

    for i in range(3):
        resultNum = num[i][0] # 점수를 선언

        for j in range(len(num[i])-1):
            resultNum *= num[i][j+1] # 스타상, 아차상을 점수에 곱함

        answer += resultNum # 최종 점수를 더함

    return answer