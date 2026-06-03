def solution(name):
    answer = 0
    n = len(name)
    # 상하 이동
    for c in name:
        up = ord(c) - ord('A')
        answer = min(up,26 - up)
        
    # 좌우 이동
    move = n-1
    for i in range(n):
        next = i+1
        
    return answer   