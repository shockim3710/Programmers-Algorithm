def solution(new_id):
    step1 = new_id.lower() # 1단계: 전부 소문자로 변경
    step2, step3_4, step4, step5, step6, answer = '', '', '', '', '', ''
    count = 0

    for i in step1: # 2단계: 특수문자가 아니고, -,_,. 아닐때
        if i.isalnum() == True or i == '-' or i == '_' or i == '.':
            step2 += i

    for i in step2: # 3, 4단계: .이 2개이상 있을때, 끝에 .이 있을때
        if i == '.':
            count += 1
        else:
            if count > 0:
                step3_4 += '.' + i
                count = 0
            else:
                step3_4 += i

    if len(step3_4) > 0 and step3_4[0] == '.': # 4단계: 처음에 .이 있을때
        step4 = step3_4[1:]
    else:
        step4 = step3_4

    if len(step4) == 0: # 5단계: 공백일때
        step5 = 'a'
    else:
        step5 = step4

    step6 = step5[0:15] # 6단계: 15자리가 넘을때
    if step6[-1] == '.': # 6단계: 끝에 .이 있을때
        step6 = step6[0:14]

    answer = step6
    if len(step6) < 3: # 7단계: 2자 이하일때
        for i in range(3-len(step6)):
            answer += step6[-1]

    return answer