"""
***로직***
1. 입력 변수
- x, y, n: 각각 주어진 수, 변환할 수, 연산 시에 필요한 수

2. 핵심 변수
- queue: BFS 연산 시에 대기열을 관리할 deque 배열 변수
- visited: 중복 연산을 피하기 위해 이미 확인한 숫자를 저장할 set 변수
- cur_res, depth: 큐에서 꺼낸 현재 연산 결과값과 현재까지의 연산 횟수 변수

3. 핵심 로직
step1: BFS 연산 준비
- 초기값과 연산 횟수를 함께 관리하기 위해 튜플을 이용하여 큐(queue) 배열 생성
- 중복 방문을 필터링하기 위해 visited 배열을 set으로 선언하고 초기값 x를 등록함

step2: 방문 탐색 및 조건 검사
- queue에서 원소를 꺼내어 파생되는 3가지 다음 값(next)을 계산함
- 계산된 next가 원하는 목표값 y와 일치하는 순간, 연산 횟수에 1을 더하여 즉시 반환함
- 일치하지 않을 시 next가 y보다 작고 visited에 존재하지 않는다면 visited에 추가 후 queue에 (next, depth + 1) 형태로 장전함

step3: 탐색 종료
- 반복문 순회가 끝날 때까지 큐가 비어버려 값이 나오지 않으면 변환 불가능으로 판단하여 -1을 반환함

4. 예외 처리
- 로직 선택: 최소 연산 횟수(최단 거리) 구하기 시 DFS 사용 시 재귀 호출 초과 및 시간 초과 현상이 발생하므로, 레벨별 확장이 보장되는 BFS를 이용하여 문제를 해결함
- 초기 주어진 수 x가 원하는 목표값 y와 처음부터 같을 시 연산 없이 함수를 조기 종료(0 반환)하도록 예외 처리함
"""

from collections import deque

def solution(x, y, n):
    if x == y:
        return 0
    
    queue = deque([(x, 0)])
    visited = set([x])
    
    while queue:
        cur_res, depth = queue.popleft()
        
        for next in [cur_res + n, cur_res * 2, cur_res * 3]:
            if next == y:
                return depth + 1
            
            if next < y and next not in visited:
                visited.add(next)
                queue.append((next, depth + 1))
                
    return -1