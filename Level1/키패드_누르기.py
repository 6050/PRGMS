def x(point):
    
    if point == '*':
        point = 10
    elif point == 0:
        point = 11
    elif point == '#':
        point = 12
        
    posX = 0
    if point % 3 == 1:
    	posX = 0
    elif point % 3 == 2:
        posX = 1
    else:
        posX = 2
        
    return posX

def y(point):
    
    if point == '*':
        point = 10
    elif point == 0:
        point = 11
    elif point == '#':
        point = 12
    
    if point / 3 <= 1:
        posY = 0
    elif point / 3 <= 2:
        posY = 1
    elif point / 3 <= 3:
        posY = 2
    else:
        posY = 3
        
    return posY

def dist(start, end):
    
    distX = abs(x(start) - x(end))
    distY = abs(y(start) - y(end))
    
    return distX + distY   

def solution(numbers, hand):
    
    answer = ''
    
    left, right = '*', '#'
    for num in numbers:
        if num in [1, 4, 7]:
            answer += 'L'
            left = num
        elif num in [3, 6, 9]:
            answer += 'R'
            right = num
        else:
            if dist(left, num) < dist(right, num):
                answer += 'L'
                left = num
            elif dist(left, num) > dist(right, num):
                answer += 'R'
                right = num
            else:
                if hand == "left":
                    answer += 'L'
                    left = num
                elif hand == "right":
                    answer += 'R'
                    right = num
                
    return answer
