def solution(board, moves):
    basket = [0] # 처음 리스트가 비어있으므로 0을 저장
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0: # 빈칸이 아니라면
                # 바구니 마지막 인형과 크레인에 잡힌 인형이 같으면
                # 2를 더하고 바구니 마지막 인형 pop
                if basket[-1] == board[j][i-1]:
                    answer += 2
                    basket.pop(-1)
                else: # 다르면 바구니에 인형 추가
                    basket.append(board[j][i-1])

                board[j][i - 1] = 0 # 크레인에 잡혔던 인형은 0으로 저장
                break

    return answer