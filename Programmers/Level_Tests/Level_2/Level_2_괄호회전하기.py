"""
***로직***
1. 입력 변수
- s: 대, 중, 소괄호로 이루어진 문자열 (길이 1 이상 1,000 이하)

2. 핵심 변수
- closer_to_opener: 닫는 괄호를 Key로, 매칭되는 여는 괄호를 Value로 둔 매핑 딕셔너리
- stack: 여는 괄호들을 쌓아두며 짝을 맞춰 폭파시킬 후입선출(LIFO) 배열
- is_valid: 현재 회전 상태의 괄호 문자열이 유효한지 체크하는 플래그 변수

3. 핵심 로직
step1: 회전 루프 제어 (외곽 for문)
- 문자열을 한 칸씩 밀어가며 전수조사해야 하므로 원본 길이인 len(s)만큼 바깥 루프를 구동함
step2: 스택 기반 괄호 유효성 검사 (내부 for문)
- 문자가 여는 괄호 유형이면 stack에 삽입(append)함
- 문자가 닫는 괄호 유형이면 스택이 비어있는지 혹은 스택 최상단(stack[-1])의 여는 괄호와 일치하는지 실시간 검사함
- 조건이 위반되는 즉시 올바르지 않은 구조로 판별(is_valid = False)하고 조기 탈출(break)함
step3: 상태 갱신 및 회전
- 내부 루프 종료 후, 유효성 플래그가 True이고 스택에 찌꺼기(닫히지 않은 여는 괄호)가 없다면 올바른 괄호 구조이므로 answer를 1 증가시킴
- 루프 말미에 s.append(s.popleft())를 수행하여 덱의 맨 앞 요소를 맨 뒤로 보내며 한 칸 회전 시뮬레이션을 구현함

4. 예외 처리
- 문자열 따옴표 오용 키 에러 방지:
  딕셔너리 참조 시 고정 문자열 use['char'] 대신 동적 루프 변수 closer_to_opener[char]를 정확하게 맵 매칭하여 예기치 못한 KeyError 및 자폭 버그를 원천 차단함
"""
from collections import deque
def solution(s):
    answer = 0
    s = deque(s)
    use = {')': '(', '}': '{', ']': '['}
    
    for i in range(len(s)):
        stack = []
        is_valid = True
        for char in s:
            if char in use.values():
                stack.append(char)
                
            elif char in use.keys():
                if not stack or stack[-1] != use[char]:
                    is_valid = False
                    break
                stack.pop()

        if not stack and is_valid == True:
            answer += 1
        
        s.append(s.popleft())

    return answer