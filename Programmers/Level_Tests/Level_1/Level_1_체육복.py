"""
***로직***
step1: 정렬
- 무작위로 값이 들어올 때를 대비해 값을 lost와 reserve를 정렬해줌
step2: 전처리
- reserve의 복사본을 순회하며 요소 i가 lost에 있는지 검사. 있다면 lost와 reserve에 요소를 삭제
step3: 결과
- reserve를 순회하며 여분이 있는 학생의 앞뒤 학생이 lost배열에 있다면 lost에서 삭제
- 전체 - lost 요소를 뺀 값을 출력
"""
def solution(n, lost, reserve):
    # 예외 처리 도난당한애가 여벌이 있을경우
    lost.sort()
    reserve.sort()
    for i in reserve[:]:
        if i in lost:
            lost.remove(i)
            reserve.remove(i)
            
    for i in reserve:
        if i-1 in lost:
            lost.remove(i-1)
        elif i+1 in lost:
            lost.remove(i+1)
            
    return n - len(lost)