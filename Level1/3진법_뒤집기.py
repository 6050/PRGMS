def solution(n):
    answer = 0
    
    rev =''
    while n > 0:
        mod = n % 3
        n //= 3
        
        rev += str(mod)
    
    answer = int(rev, 3)
    
    return answer
