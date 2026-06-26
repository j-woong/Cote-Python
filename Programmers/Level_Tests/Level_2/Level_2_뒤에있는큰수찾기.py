"""
***로직***
1. 입력 변수
- numbers: 반복문을 순회하며 앞선 값이 뒤에 올 값보다 큰지 비교하는 기준이 되는 리스트
2. 핵심 변수
- stack: 아직 자기보다 큰 수를 만나지 못한 인덱스들을 임시 저장할 대기열 배열 변스
- target_idx: 현재 값보다 작은 값을 가진 스택 최상단(top) 인덱스를 추출하여 저장하는 변수
- answer: numbers 배열의 갯수만큼 -1로 초기화하여 조건에 부합하면 해당 인덱스의 값을 변화시키고 최종적으로 정답을 반환하는 배열

3. 핵심 로직
step1: 초기값 세팅 및 스택 생성
- 초기값을 -1을 가지는 len(numbers) 크기의 answer 배열 생성
- 인덱스를 비교 및 보관할 빈 stack 배열 생성
step2: 리스트 순회 및 값 비교
- numbers를 순회하며 스택에 현재 인덱스를 추가
- 만약 스택이 비어있지 않고 스택의 top인덱스의 numbers값이 현재 numbers 값보다 작다면 스택의 top인덱스를 추출하여 answer[top인덱스]에 현재 numbers값을 대입
step3: 정답 반환
- 반복문 순회가 끝나면 결과 answer 배열을 반환함

4. 예외 처리
이중 중첩문 사용 시 O(N^2)의 시간 복잡도로 인해 데이터 100만 개 기준 약 5,000억 번의 연산이 유발되어 시간 초과가 발생함
- 단조 스택(Monotonic Stack) 구조를 활용해 각 원소의 삽입 및 삭제를 O(1)로 제어하여 전체 로직을 O(N)으로 압축하고 시간 초과 예외를 해결함
"""
def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []
    
    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            target_idx = stack.pop()
            answer[target_idx] = numbers[i]
            
        stack.append(i)
        
    return answer