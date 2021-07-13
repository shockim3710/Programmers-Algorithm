def solution(numbers, hand):
    keyPad = {1:[0, 0], 2:[1, 0], 3:[2, 0],
              4:[0, 1], 5:[1, 1], 6:[2, 1],
              7:[0, 2], 8:[1, 2], 9:[2, 2],
            '*':[0, 3], 0:[1, 3], '#':[2, 3]}
    leftHand = '*' # 현재 왼손위치
    rightHand = '#' # 현재 오른손위치
    answer = ''

    for i in numbers:
        # 번호가 왼쪽에 있을때 answer에 L추가, 왼손에 번호저장
        if keyPad[i][0] == 0:
            leftHand = i
            answer += 'L'
        # 번호가 오른쪽에 있을때 answer에 R추가, 오른손에 번호저장
        elif keyPad[i][0] == 2:
            rightHand = i
            answer += 'R'
        # 번호가 가운데에 있을때 손에 저장된 번호와 거리계산
        elif keyPad[i][0] == 1:
            x = abs(keyPad[i][0]-keyPad[leftHand][0]) + \
                abs(keyPad[i][1]-keyPad[leftHand][1])
            y = abs(keyPad[i][0]-keyPad[rightHand][0]) + \
                abs(keyPad[i][1]-keyPad[rightHand][1])
            # 거리가 오른손이 멀거나, 같은데 왼손잡이일때
            if x < y or (x == y and hand == "left"):
                leftHand = i
                answer += 'L'
            # 거리가 왼손이 멀거나, 같은데 오른손잡이일때
            elif x > y or (x == y and hand == "right"):
                rightHand = i
                answer += 'R'

    return answer