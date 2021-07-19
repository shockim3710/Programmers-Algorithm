def solution(s):
    numWord = {'zero' : 0, 'one' : 1, 'two' : 2, 'three' : 3,
               'four' : 4, 'five' : 5, 'six' : 6, 'seven' : 7,
               'eight' : 8, 'nine' : 9} #  숫자에 대응되는 영단어
    word = '' # s의 영단어 한글자씩 추가
    answer = '' # 문자로 더하기위해 문자로 선언

    for i in s:
        # s가 숫자이면 answer에 문자로 더함
        if i.isdigit() == True:
            answer += i
        # 숫자가 아니면 한글자씩 문자로 더함
        else:
            word += i
            # 더해진 글자가 영단어 안에 있으면
            # 대응되는 숫자를 answer에 문자로 더함
            if word in numWord:
                answer += str(numWord[word])
                word = '' # 영단어 초기화

    answer = int(answer) # 문자에서 숫자로 변환

    return answer