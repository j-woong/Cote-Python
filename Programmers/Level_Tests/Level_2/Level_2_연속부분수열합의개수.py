"""
***로직***
1. 입력 변수
- elements: 원형 수열의 각 원소들이 담긴 배열 (길이 3 이상 1,000 이하)

2. 핵심 변수
- n: 원본 수열의 고유 길이
- extended_elements: 원형 구조를 일렬로 펼치기 위해 원본 배열을 2배로 늘린 확장 배열 (elements * 2)
- set_A: 부분 수열들의 합을 저장하며, 중복된 합은 자동으로 걸러내 줄 set(집합) 자료구조
- seq_sum: j번 인덱스부터 시작해서 길이 i만큼 잘라낸 연속 부분 수열의 합

3. 핵심 로직
step1: 원형 구조의 선형화
- 맨 뒤 원소와 맨 앞 원소가 이어지는 원형 수열의 특성을 인덱스 에러 없이 처리하기 위해, elements를 2배로 복사한 extended_elements를 생성함
step2: 슬라이싱 구간 합 누적
- 외곽 루프 i: 부분 수열의 '길이'를 1부터 n까지 1씩 증가시키며 제어함
- 내부 루프 j: 부분 수열이 시작될 '시작 인덱스' 위치를 0부터 n-1까지 순회함
- extended_elements[j : j + i] 구간을 정확하게 자른 뒤, sum() 함수로 연속된 합(seq_sum)을 구해 set_A에 삽입(add)함
step3: 결과 반환
- set 자료구조의 특성 덕분에 아무리 많은 중복 합이 들어와도 유일한 값들만 남게 되므로, 최종적으로 set_A의 크기(len)를 반환함

4. 예외 처리
- 조합(Combinations)의 오류 방지 및 연속성 유지:
  무작위로 원소를 뽑아내는 단순 조합 연산 대신, 2배 늘린 배열에서 순차적으로 '슬라이싱 구간 합'을 구하는 방식을 채택하여 원형 수열의 연속성 규칙과 예외 구간(맨 끝 + 맨 앞)을 완벽하게 방어함

"""
def solution(elements):
    n = len(elements)
    extended_elements = elements * 2
    set_A = set()
    
    for i in range(1,n+1):
        for j in range(n):
            seq_sum = sum(extended_elements[j:j+i])
            set_A.add(seq_sum)
            
    return len(set_A)