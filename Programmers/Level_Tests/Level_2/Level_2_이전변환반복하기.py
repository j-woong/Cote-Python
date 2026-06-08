def solution(s):
    answer = [0,0]
    
    def binary(num):
        if num == 0: return "0"
        res = ''
        
        while num > 0:
            res += str(num % 2)
            num = num // 2
        return res[::-1]
        
    while s != '1':
        res = ''
        cnt = 0
        for c in s:
            if c == '0':
                cnt += 1
            else:
                res += '1'
    
        answer[0] += 1
        answer[1] += cnt
        
        s = binary(len(res))

    return answer