"""
***로직***
1. 입력 변수
- arr1,arr2: 행렬 곱셈 연산에 필요한 2차원 배열

2. 핵심 변수
- row: arr1의 행 개수이며 결과 행렬의 세로 크기를 결정할 변수
- col: arr2의 열 개수이며 결과 행렬의 가로 크기를 결정할 변수
- match: 앞 행렬의 열이자 뒤 행렬의 행 크기이며 삼중 루프 내부에서 동기화되어 움직일 공통 범위 변수
- s: 행렬의 원소끼리 곱한 값을 실시간으로 누적해서 더해나갈 변수
- R: 하나의 가로줄 계산이 끝날 때마다 결과 원소들을 묶어서 answer에 추가할 임시 리스트 변수
- answer: 행렬 곱연산 완료 후 최종적으로 반환할 빈 2차원 행렬 변수

3. 핵심 로직
step1: 행렬 스케일 정의
- len(arr1)로 row를 구하고 len(arr2[0])으로 col을 구하며 len(arr2)로 match 크기를 정의함

step2: 삼중 루프 연산
- i 루프로 row만큼, j 루프로 col만큼, k 루프로 match만큼 도는 삼중 루프를 구성함
- i 루프가 돌 때마다 가로줄을 담을 임시 리스트 R을 초기화함
- j 루프가 돌 때마다 누적할 변수 s를 0으로 초기화함
- k 루프를 돌며 arr1[i][k]와 arr2[k][j]를 정방향으로 곱하여 s에 누적해서 더해줌

step3: 정답 출력
- k 루프가 끝나면 계산된 원소 s를 R에 추가함
- j 루프가 끝나면 완성된 가로줄 R을 answer에 추가함
- 모든 루프가 종료되면 최종 완성된 2차원 행렬 answer를 반환함

4. 예외 처리
- 변수명 중복 오염 방지: 이전 코드에서 발생했던 행 개수 변수와 임시 리스트 변수의 이름 충돌을 row와 R로 명확히 분리하여 형식 에러를 차단함
- 정방향 인덱스 매칭: 컴퓨터 메모리 구조에 맞춰 인덱스를 뒤집지 않고 k를 정방향으로 그대로 사용하여 수학적 행렬곱 규칙을 유지함
"""

def solution(arr1, arr2):
    answer = []
    row = len(arr1)
    col = len(arr2[0])
    match = len(arr2)

    for i in range(row):
        R = []
        for j in range(col):
            s = 0
            for k in range(match):
                s += arr1[i][k]*arr2[k][j]
            R.append(s)
        answer.append(R)
    return answer

# 재풀이
def solution(arr1, arr2):
    row = len(arr1) 
    col = len(arr2[0])
    match = len(arr2)
    
    matrix = [[ 0 for j in range(col)] for i in range(row)]
    
    for i in range(row):
        for j in range(col):
            for k in range(match):
                matrix[i][j] += (arr1[i][k] * arr2[k][j])
                
            
    return matrix