"""
***로직***
1. 입력 변수
- k: 유저의 현재 남은 피로도
- dungeons: 최소 필요 피로도와 소모 피로도가 담긴 2차원 배열

2. 핵심 변수
- visited: 특정 던전을 탐색 경로에서 이미 방문했는지 체크하는 방문 배열
- cnt: 현재 경로에서 클리어한 던전의 개수를 누적하는 변수
- answer: 전수조사를 하며 갱신되는 최대 던전 클리어 횟수를 담는 변수이며 nonlocal로 제어

3. 핵심 로직
step1: 상태 정의 및 초기화
- 어떤 던전을 먼저 가느냐에 따라 뒤이어 갈 수 있는 던전의 선택지가 달라지므로 모든 경우의 수를 구하는 완전 탐색 DFS 백트래킹을 선택함
- 던전의 최대 개수가 8개로 매우 작기 때문에 브루트 포스가 가능함
- 던전의 수만큼 False로 초기화된 visited 배열을 생성함
step2: 재귀적 백트래킹 탐색
- 함수가 호출될 때마다 현재 클리어 횟수를 기존 answer와 비교하여 더 큰 값으로 최댓값을 실시간 갱신함
- enumerate 함수로 던전들을 순회하며 아직 방문하지 않았고 현재 피로도가 최소 필요 피로도 이상인 던전을 탐색함
step3: 상태 플래그 제어 및 복원
- 조건을 만족하는 던전을 찾으면 visited 배열의 해당 인덱스를 True로 변경하여 상태를 잠금
- 피로도를 차감하고 클리어 카운트를 늘려 다음 재귀 호출을 진행함
- 해당 깊이의 탐색이 끝나고 부모 노드로 복귀할 때 다른 경로에서 이 던전을 다시 탐색할 수 있도록 visited 배열의 해당 인덱스를 다시 False로 원상복구함

4. 예외 처리
- 탐욕법의 오류 방지
단순히 소모 피로도가 적은 순서나 최소 피로도가 높은 순서로 정렬해서 풀면 최적의 해를 보장할 수 없으므로 백트래킹을 통해 모든 순열을 탐색하도록 설계하여 예외 케이스를 완벽하게 차단함
"""
def solution(k, dungeons):
    answer = 0
    visited = [False] * len(dungeons)
    
    def dfs(k,cnt):
        nonlocal answer
        answer = max(answer,cnt)
        
        for i, (min_p,consum_p) in enumerate(dungeons):
            if not visited[i] and min_p <= k:
                visited[i] = True
                dfs(k-consum_p, cnt + 1)
                visited[i] = False
    
    dfs(k,0)
    return answer