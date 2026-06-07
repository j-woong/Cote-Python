def solution(s):
    answer = []
    ss = s.split(" ")
    
    for s in ss:
        jaden_s = ''
        jaden_s += s[0:1].upper() + s[1:].lower()
        
        answer.append(jaden_s)
            
    return " ".join(answer)