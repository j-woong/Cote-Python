"""
***로직***
1. 입력 변수
- dirs: 명령어 U, R, D, L이 순서대로 담긴 문자열

2. 핵심 변수
- r, c: 캐릭터의 현재 위치 좌표를 나타내며 초기값은 중앙인 5, 5 세팅
- dr, dc: 상우하좌 방향 이동에 따른 행과 열의 변화량을 담은 델타 배열
- URDL: 문자에 따른 델타 인덱스를 매칭한 딕셔너리
- visited_edges: 지나간 양방향 경로 자체를 중복 없이 저장할 set 변수

3. 핵심 로직
step1: 방향성 및 범위 제어
- dirs 문자열을 순회하며 현재 좌표에 델타 값을 더해 다음 예상 좌표인 next_r, next_c를 계산함
- 계산된 좌표가 0 이상 10 이하의 유효한 11x11 격자 경계 내에 존재하는지 우선 검사함

step2: 양방향 선 간선 유효성 검사
- 경계를 만족하면 현재 좌표와 다음 좌표를 잇는 정방향 간선과 역방향 간선 쌍을 생성함
- set의 O(1) 탐색을 활용해 해당 간선이 visited_edges에 존재하지 않는 최초 방문인지 판별함
- 처음 걷는 길이라면 정방향과 역방향 경로를 모두 set에 add 함수로 등록함

step3: 좌표 갱신 및 결과 출력
- 조건 성립 여부와 관계없이 캐릭터의 위치를 next_r, next_c로 이동시킴
- 모든 명령 수행이 끝나면 양방향 경로가 누적된 세트의 총 길이를 2로 나눈 몫을 최종 걸어본 길의 길이로 반환함

4. 예외 처리
- 인덱스 에러 사전 방단: 좌표 조회가 경계 검사보다 먼저 실행되어 터지던 구조를 탈피하고 범위 검증을 최우선 분기문으로 배치하여 안정성을 확보함
- 점과 선의 도메인 분리: 방문 여부를 정점이 아닌 간선 자체로 관리하고 역방향 경로까지 동시에 묶어 처리함으로써 왕복 및 중복 경로 카운트 예외를 완벽히 차단함
"""
def solution(dirs):
    visited_edges = set()
    
    r, c = 5,5
    dr = [-1,0,1,0]
    dc = [0,1,0,-1]
    URDL = { 'U': 0, 'R': 1, 'D': 2, 'L': 3}
    
    for dir in dirs:
        next_r, next_c = r + dr[URDL[dir]], c + dc[URDL[dir]]
        
        if 0 <= next_r <= 10 and 0 <= next_c <= 10:
            edges1 = ((r, c), (next_r,next_c))
            edges2 = ((next_r, next_c), (r,c))
            
            if not edges1 in visited_edges:
                visited_edges.add(edges1)
                visited_edges.add(edges2)
            
            r,c = next_r, next_c
            
    return len(visited_edges) // 2