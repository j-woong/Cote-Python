"""
***로직***
1. 입력 변수
- citations: 연구자가 제출한 각 논문의 인용 횟수가 담긴 파이썬 리스트 (길이 1 이상 1,000 이하)

2. 핵심 변수
- n: 연구자가 쓴 총 논문의 개수 (len(citations))
- h: 현재 조사 중인 논문 위치에서 가질 수 있는 유효 H-index 후보값
- answer: 루프를 돌며 갱신되는 최종 최대 H-index 값

3. 핵심 로직
step1: 데이터 정렬 및 스케일 정의
- 인용 횟수를 기준으로 논문들을 오름차순(citations.sort()) 정렬함
- 정렬을 수행함으로써 특정 인덱스 i 이후의 논문들은 모두 최소 citations[i]번 이상 인용되었음을 보장받게 됨
step2: 선형 탐색 및 H-index 후보군 추출 (for i in range(n))
- i번 인덱스 논문 기점으로 '현재 논문의 인용 횟수(citations[i])'와 '이보다 많이 인용된 남은 논문의 개수(n - i)'를 비교함
- 두 값 중 더 작은 값(min)을 취해, 해당 지점에서 안전하게 성립 가능한 H-index 후보인 h를 도출함
step3: 최댓값 갱신 및 반환
- 매 루프마다 현재까지의 answer와 새로 구한 h 중 더 큰 값(max)으로 answer를 지속 갱신함
- 전수조사가 완료되면 최종 누적된 answer 값을 반환함

4. 예외 처리
- 인용 횟수가 논문 수보다 압도적으로 많은 엣지 케이스 방어:
  예를 들어 [10, 20, 30] 처럼 인용 횟수가 매우 높아도 논문 개수가 3개라면 H-index는 3을 넘을 수 없음. min(n-i, citations[i]) 장치가 이 한계선을 정밀하게 잡아주므로 인용 횟수의 스케일에 상관없이 완벽하게 무결성을 보장함
  """
def solution(citations):
    answer = 0
    citations.sort()
    n = len(citations)
    
    
    for i in range(n):
        h = min(n-i,citations[i])
        answer = max(answer,h)

    return answer