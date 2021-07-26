def solution(phone_number):
    # *을 전체 번호길이에서 4를 뺀 길이만큼 추가하고
    # 그 뒤에 뒷 4자리만 인덱싱하여 추가
    answer = '*'*(len(phone_number)-4) + phone_number[len(phone_number)-4::]
    return answer