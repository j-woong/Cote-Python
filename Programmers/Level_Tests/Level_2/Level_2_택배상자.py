"""
***로직***
1. 입력 변수
- order: 택배 기사님이 원하는 상자의 순서가 담긴 정수 배열

2. 핵심 변수
- support: 메인 벨트에서 내린 상자들을 임시 보관할 보조 컨테이너 벨트 스택 배열
- idx: 메인 컨테이너 벨트에서 현재 대기 중인 상자의 번호를 가리킬 포인터 정수 변수
- answer: 트럭에 무사히 실린 택배상자의 총 개수를 누적할 변수

3. 핵심 로직
step1: 순차 탐색 및 메인 벨트 제어
- order 배열의 원하는 상자 번호 R을 순차적으로 순회함
- 현재 메인 벨트 포인터 idx가 R보다 작다면, 조건을 만족할 때까지 idx를 support 스택에 삽입(append)하고 idx를 1씩 증가시킴

step2: 타겟 상자 비교 및 이관
- 메인 벨트의 포인터 idx가 R과 일치하면 트럭에 적재 처리를 수행하여 answer를 1 증가시키고 idx를 다음 상자로 넘김
- 만약 메인 벨트에 없다면 보조 벨트 스택이 비어있지 않고 최상단(top) 원소가 R과 일치하는지 검사하여, 일치 시 pop 연산 후 answer를 1 증가시킴

step3: 예외 탈출 및 결과 반환
- 메인 벨트의 포인터와 보조 벨트의 top 원소 둘 다 R을 만족하지 못하면 더 이상 상자를 실을 수 없는 불가능 상태이므로 즉시 반복문을 완전히 탈출(break)함
- 모든 과정이 종료되면 최종 적재 개수인 answer 값을 반환함

4. 예외 처리
- 불필요한 전체 리스트 생성 오버헤드 및 탐색 고립 차단:
  메인 벨트 전체를 2차원 리스트로 역순 생성하는 낭비를 변수 포인터 제어로 압축하고, 메인 벨트 고갈 시 보조 벨트 검사가 불가능해지던 루프 종속 예외를 분기별 독립 검사로 재설계하여 안정성을 확보함
"""
def solution(order):
    answer = 0
    idx = 1
    support = []

    for R in order:
        while idx <= len(order) and idx < R:
            support.append(idx)
            idx += 1
            
        if idx == R:
            answer += 1
            idx += 1
        elif support[-1] == R:
            support.pop()
            answer += 1
        else:
            break
    return answer