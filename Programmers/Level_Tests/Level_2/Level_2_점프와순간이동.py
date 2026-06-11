def solution(n):
    B = 0
    
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n -= 1
            B += 1
    
    return B + 1