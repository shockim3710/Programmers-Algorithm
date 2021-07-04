def solution(a, b):
    answer = ''

    if a == 1: # 1월일 때
        count = b
    elif a == 2: # 2월일 때
        count = 31 + b
    else:
            count = 31 + 29 + b

            for i in range(3, a):
                # 3월부터 7월까지는 짝수달 30일 홀수달 31일
                if i < 8:
                    if i % 2 != 0:
                        count += 31
                    else:
                        count += 30

                # 8월부터 12월까지는 짝수달 31일 홀수달 30일
                elif i > 7:
                    if i % 2 != 0:
                        count += 30
                    else:
                        count += 31

    if count%7 == 1:
        answer = 'FRI'
    elif count%7 == 2:
        answer = 'SAT'
    elif count%7 == 3:
        answer = 'SUN'
    elif count%7 == 4:
        answer = 'MON'
    elif count%7 == 5:
        answer = 'TUE'
    elif count%7 == 6:
        answer = 'WED'
    elif count%7 == 0:
        answer = 'THU'

    return answer