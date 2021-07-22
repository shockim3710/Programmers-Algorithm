def solution(s):
    s = s.lower() # 전부 소문자로 변경

    if s.count('p') != s.count('y'):
        return False
    else:
        return True