def solution(arr):
    stack = [arr[0]]
    
    for n in arr:
        if stack and stack[-1] != n:
            stack.append(n)  
            
    return stack