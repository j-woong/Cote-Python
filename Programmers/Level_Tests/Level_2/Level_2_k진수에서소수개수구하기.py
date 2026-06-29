"""
***로직***
1. 입력 변수
- n: 소수를 검사할 대상이 되는 10진수 정수
- k: 변환하고자 하는 진수 기준 정수

2. 핵심 변수
- target: 10진수 n을 k진수로 변환 완료한 문자열 변수
- words: target 문자열을 '0' 기준으로 쪼개어 담은 분리 배열 변수
- answer: 분리된 숫자 중 소수 조건에 부합하는 개수를 누적할 변수

3. 핵심 로직
step1: 진수 변환 연산
- k가 10일 때는 str(n)을 바로 취하고, 그 외에는 나머지(%)와 몫(//) 연산 기반의 역순 빌드업을 통해 k진수 문자열 target을 생성함

step2: 문자열 분리 및 파싱
- 파이썬의 split('0') 함수를 사용하여 '0'을 기점으로 문자열을 일괄 분리하여 words 배열에 저장함
- 연속된 '0'으로 인해 발생할 수 있는 빈 문자열('')을 예외 필터링하기 위해 분기문을 구성함

step3: 소수 판별 및 결과 출력
- 추출된 유효 숫자 문자열을 int형으로 변환 후 제곱근 범위인 int(n**0.5)+1 까지 나누어떨어지는지(%) 탐색하는 소수 판별식(isPrime)을 구동함
- 소수임이 판명되면 answer 개수를 1 증가시키고 모든 순회가 끝나면 최종 값을 반환함

4. 예외 처리
- 연산자 우선순위 및 타겟 바인딩 오류 방지:
  거듭제곱 연산 순위 혼선(n**1/2+1)과 문자열 리터럴 표기('char')로 인한 런타임 에러를 정상 제어하고, 문자열 수동 파싱 시 발생하는 마지막 자리 누락 예외를 split 함수 도입을 통해 원천 차단함
"""
def to_k(n,k):
    res = ""
    while n >= k:
        remain = n % k
        res += str(remain)
        n = n // k

    res += str(n)
    return res[::-1]
    
def isPrime(n):
    if n < 2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
    
def solution(n, k):
    answer = 0
    # 진수 변환 함수 -> int('n',k)
    target = str(n) if k == 10 else to_k(n,k)
    
    words = target.split('0')
    print(words)
    for w in words:
        if w != "":
            if isPrime(int(w)):
                answer += 1
            
    return answer