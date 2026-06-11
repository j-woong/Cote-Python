"""
***로직***
1. 입력 변수
- k: 최소 방법을 고려히야 선택할 귤의 개수
- tangerine: 뽑을 귤의 서로 다른 크기의 귤이 담긴 배열
2. 핵심 변수 
- answer: 최소 방법의 가짓수
- table: {귤의 크기:귤의 개수} 값을 가진 카운터 함수를 이용한 해시
- val_list: table의 값들의 내림차순 배열
3. 핵심 로직
step1: 빈도수 추출 및 내림차순 정렬
- 카운터함수를 이용한 해시 테이블 생성
- table.values()를 내림차순으로 정렬하여 val_list 배열 생성
step2: 순회 및 방법 카운트
- val_list를 순회하여 k가 0보다 크면 계속 반복문을 순회하면서 종류 수를 1개씩 증가시킴
step3: 조기 탈출 및 반환
- 만약 k가 0 이라면 반복문들 빠져나오고 answer를 반환함
4. 예외 처리
대규모 오버헤드 방지:
- 조합이나 완전탐색(DFS)를 사용할 경우 O(n^2)의 지수 시간복잡도로 인해 시간 및 메모리 초과가 발생하여, 정렬O(Nlog N))과 O(n)의 시간복잡도를 가진 그리디 알고리즘을 사용

"""
from collections import Counter
def solution(k, tangerine):
    answer = 0
    table = Counter(tangerine)
    
    val_list = sorted(table.values(),reverse=True)
    
    for val in val_list:
        if k <= 0:
            break
        
        k -= val
        answer += 1
    
    return answer