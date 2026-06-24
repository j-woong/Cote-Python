"""
***로직***
1. 입력 변수
- topping: 롤케이크에 얹힌 토핑들의 번호가 순서대로 담긴 배열

2. 핵심 변수
- brother: 동생이 가진 토핑의 종류와 개수를 실시간으로 관리할 Counter 딕셔너리 변수
- chulsoo: 형이 가진 토핑의 종류를 중복 없이 담아낼 set 변수
- answer: 형과 동생의 토핑 종류 수가 동일해지는 공평한 방법의 가짓수를 담을 변수

3. 핵심 로직
step1: 초기 상태 세팅
- 처음에는 동생이 롤케이크의 모든 토핑을 다 가졌다고 가정하고 Counter를 이용해 전수 집계함
- 형의 토핑 주머니인 chulsoo set를 빈 상태로 초기화함

step2: 선형 탐색 및 토핑 이관 연산
- topping 배열을 처음부터 하나씩 정방향으로 순회하며 형의 set에 토핑을 하나씩 추가함
- 동생의 딕셔너리에서는 방금 형이 가져간 토핑의 개수를 1만큼 차감함
- 차감 후 동생 주머니의 해당 토핑 개수가 0개가 되면 len 연산에 영향을 주지 않도록 딕셔너리에서 키를 완전히 삭제함

step3: 정답 출력
- 매 루프마다 len(chulsoo) 값과 len(brother) 값을 실시간 비교하여 두 종류 수가 완벽히 일치하면 answer를 1 증가시킴
- 순회가 모두 끝나면 최종 누적된 answer 값을 반환함

4. 예외 처리
- 슬라이싱 및 중복 set 생성 오버헤드 차단: 
  배열의 최대 크기가 100만이므로 루프 내부에서 매번 자르고 set을 만들면 O(N^2)으로 터짐을 인지하고 개수 증감 연산 방식인 O(N)으로 압축하여 효율성 테스트를 완벽히 통과함
"""

from collections import Counter
def solution(topping):
    answer = 0
    brother = Counter(topping)
    chulsoo = set()
    
    for t in topping:
        chulsoo.add(t)
        brother[t] -= 1
        
        if brother[t] == 0:
            del brother[t]
            
        if len(chulsoo) == len(brother):
            answer += 1
        
        
    return answer