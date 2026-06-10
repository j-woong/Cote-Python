"""
***로직***
1. 입력 변수
- n: 표현하고자 하는 목표 자연수

2. 핵심 변수
- answer: 연속된 자연수로 n을 만들수있는 방법의 수
- total: i부터 시작해서 j까지 연속으로 더해나가는 누적 합계

3. 핵심 로직
step1: 탐색 범위 최적화
- 연속된 수의 합으로 n을 만들 때, 시작번호 i는 절반을 넘길 수 없으므로 범위 끝을 (n+1)//2로 정해둠
step2: 이중 루프 누적 탐색 및 분기 탈출
- 루프 시작을 i부터 시작해서 연속해서 total에 j를 더해나감
- 만약 total이 n과 같아지면 루프를 answer를 1 올리고 안쪽루프를 빠져나감
- 만약 total이 n보다 커지면 바로 안쪽루프를 빠져나감

4. 예외 처리
- 루프가 n의 절반까지밖에 안돌기 때문에 자기자신일 때를 대비해 answer에 1을 더해 반환함
"""
def solution(n):
    answer = 0
    
    for i in range(1,(n+1)//2):
        total = 0
        for j in range(i,(n+1)//2+1):
            total += j
            if total > n:
                break
            elif total == n: 
                answer += 1
                break
    
    return answer+1