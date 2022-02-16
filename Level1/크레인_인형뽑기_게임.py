def solution(board, moves):
    
    basket = []
    answer = 0
    
    for i in moves:
        for floor in range(len(board)):
            if board[floor][i-1] == 0:
                pass
            else:
                basket.append(board[floor][i-1])
                board[floor][i-1] = 0
                break
        if len(basket) >= 2:
            if basket[-1] == basket[-2]:
                basket = basket[:-2]
                answer += 2
            
    return answer
