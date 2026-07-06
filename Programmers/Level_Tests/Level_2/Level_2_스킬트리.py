"""
***로직***
1. 입력 변수
- skill: 선행 스킬 순서가 담긴 문자열 변수
- skill_trees: 유저들이 찍은 스킬트리들이 담긴 문자열 배열

2. 핵심 변수
- replica: 각 스킬트리 문자열에서 선행 스킬과 관련 없는 알파벳을 제거해 나갈 임시 문자열 변수
- answer: 올바른 순서로 작성된 스킬트리의 총 개수를 누적할 변수

3. 핵심 로직
step1: 비관련 알파벳 필터링
- skill_trees를 순회하며 각 스킬트리를 replica 변수에 복사함
- 문자열 내부를 하나씩 조회하며 해당 알파벳이 skill 내에 포함되어 있지 않다면 replace 함수를 구동함
- 파이썬 문자열 불변 특성에 따라 replica = replica.replace(c, '') 형태로 연산 결과를 실시간 덮어쓰기함

step2: 선행 스킬 순서 일치 검사
- 필터링이 끝난 replica의 길이를 측정함
- skill 문자열을 앞에서부터 replica의 길이만큼 슬라이싱(skill[:len(replica)])하여 두 문자열이 완벽히 일치하는지 비교함

step3: 결과 반환
- 일치 조건 충족 시 answer를 1 증가시키고, 전체 순회가 종료되면 최종 개수를 반환함

4. 예외 처리
- 문자열 불변(Immutable) 객체 제어 및 불완전 포함 관계 차단:
  replace 함수의 반환값을 재할당하지 않아 원본 문자열이 유지되던 버그를 변수 덮어쓰기로 교정하고, 단순 in 키워드 탐색 시 발생하던 중간 순서 진입 예외("BD" 등)를 전방 자릿수 슬라이싱 비교 방식으로 전환하여 무결성을 보장함
"""
def solution(skill, skill_trees):
    answer = 0 
    
    for s in skill_trees:
        replica = s
        for c in s:
            if c not in skill:
                replica = replica.replace(c, '')
        
        if skill[:len(replica)] == replica:
            answer += 1
        
    return answer