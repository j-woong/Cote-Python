"""
***로직***
1. 입력 변수
- people: 사람들의 몸무게를 담은 배열
- limit: 구명보트의 무게 제한

2. 핵심 변수
- left: 가장 가벼운 사람을 가리키는 시작 포인터 (0번 인덱스)
- right: 가장 무거운 사람을 가리키는 시작 포인터 (맨 끝 인덱스)
- answer: 사용된 구명보트 개수 (카운터)

3. 핵심 로직
step1: 오름차순 정렬
- 효율적인 매칭을 위해 우선 people 배열을 몸무게 순으로 정렬
step2: 투 포인터 양방향 순회
- while left <= right 조건을 걸어 두 포인터가 서로 만나거나 교차해서 엇갈릴 때까지 루프 돌림
step3: 그리디 보트 매칭 및 포인터 전진
- 가장 가벼운 사람과 가장 무거운 사람의 합(people[left] + people[right])이 limit 이하인지 체크
- 조건 만족하면 둘 다 태워 보낼 수 있으므로 left += 1, right -= 1 처리
- 무게 초과하면 무거운 사람 혼자 타야 하므로 right -= 1만 처리
step4: 보트 카운트
- 매칭 결과랑 상관없이 보트는 매 루프마다 무조건 1대씩 출발하므로 answer += 1 일괄 적용

4. 예외 처리
- 홀수 인원 및 인덱스 꼬임 방지 (while left <= right):
  조건을 'left < right'가 아니라 같을 때까지 포함시켜서, 마지막에 홀수 인원이 남아 'left == right'가 되는 순간(마지막 1명 남음)에도 루프가 정상 작동해 혼자 보트 태워서 안전하게 끝내도록 예외 처리함
- 시간 복잡도 최적화:
  배열 원소를 실제로 삭제하는 pop(0)이나 이중 for문을 절대 배제하고, 인덱스 포인터만 제어하는 방식으로 O(N^2) 시간 초과 원천 차단
"""
def solution(people, limit):
    answer = 0
    people = sorted(people)
    
    left = 0
    right = len(people)-1
    while right >= left:
        if left == right:
            answer += 1
            break
        if people[left] + people[right] <= limit:
            answer += 1
            left += 1
            right -= 1
        else:
            answer += 1
            right -= 1
    return answer