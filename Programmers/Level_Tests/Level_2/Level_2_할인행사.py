from collections import Counter
def solution(want, number, discount):
    answer = 0
    product = Counter(want)
    for i in range(len(want)):
        product[want[i]] = number[i]
    
    for i in range(len(discount)-9):
        Cdiscount = Counter(discount[i:i+10])
        if not product-Cdiscount:
            answer += 1
            
    return answer