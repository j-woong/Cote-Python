"""
***로직***
1. 입력 변수
- n: 2진수로 변환하고자 하는 타겟이 되는 자연수

2. 핵심 변수
- target: 2진수로 변환하여 가지고 있는 '1'의 갯수
- next_n: n과 가장 가까운 자연수를 찾을때 1씩 증가시키는 자연수

3. 핵심 로직
step1: 기준 변수 생성
- 찾고자하는 이진수의 타겟 1을 bin(), count()함수를 이용해 target 변수 생성
step2: 목표 변수 탐색
- while문을 통해 n의 다음 변수인 next_n을 이진수 변환bin()와 count 함수로 1의 갯수를 탐색
- 갯수가 같다면 next_n 자체를 반환

4. 예외 처리
- n의 범위는 1,000,000이기 때문에 O(n)의 시간복잡도를 가진 반복문을 중첩 사용 시 시간초과 발생ㅋ
"""
def solution(n):
    target = bin(n).count('1')
    next_n = n+1
    
    while True:
        if bin(next_n).count('1') == target:
            
            return next_n
        next_n += 1
