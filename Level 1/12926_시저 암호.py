def solution(s, n):
    answer = ''

    for i in s:
        if i == ' ': # 공백은 그대로 answer에 추가
            answer += ' '
        else:
            # 아스키코드가 z를 넘어가면
            # 모듈러를 하여 a위치에서 밀어짐
            if ord(i) + n > 122:
                answer += chr((ord(i) + n) % 122 + 96)
            # 아스키코드가 Z를 넘어가고 대문자이면
            # 모듈러를 하여 A위치에서 밀어짐
            elif ord(i) + n > 90 and i.isupper() == True:
                answer += chr((ord(i) + n) % 90 + 64)
            else: # 아스키코드에서 n만큼 밀어짐
                answer += chr(ord(i) + n)

    return answer