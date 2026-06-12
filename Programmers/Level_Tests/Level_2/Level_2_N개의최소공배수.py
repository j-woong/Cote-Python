"""
***로직***
1. 입력 변수
- arr: 최소공배수를 구하고자 하는 자연수들이 담긴 수열 (길이 1 이상 15 이하)

2. 핵심 변수
- lcm_num: 수열을 순회하며 매 순간 갱신되는 누적 최소공배수
- reduce(): 여러 개의 원소가 담긴 시퀀스를 하나의 값으로 누적 압축하는 파이썬 내장 함수

3. 핵심 로직
step1: 초기값 설정
- 수열의 첫 번째 원소(arr[0])를 초기 누적 최소공배수(lcm_num)로 설정함
step2: 순차적 누적 탐색 (for문)
- 1번 인덱스부터 끝까지 순회환며, '현재까지의 누적 최소공배수(lcm_num)'와 '새로 만난 수(arr[i])'의 최소공배수를 math.lcm() 함수로 구함
step3: 값 갱신 및 반환
- 계산된 새로운 최소공배수로 lcm_num을 갱신하고, 루프가 끝나면 최종 누적값을 반환함

4. 예외 처리
- 원소가 1개인 수열 방어:
  수열의 길이가 1일 경우, 기본 풀이에서는 for문이 돌지 않고 arr[0]이 그대로 반환되며, reduce 풀이 역시 누적할 다음 원소가 없으므로 arr[0]을 그대로 반환하여 인덱스 에러나 누수 없이 안전하게 구동됨
"""
import math
from functools import reduce
def solution(arr):
    
    return reduce(lambda x,y: (x*y) // math.gcd(x,y),arr)
    
"""import math
def solution(arr):
    
    lcm_num = arr[0]
    for i in range(1,len(arr)):
        lcm_num = math.lcm(lcm_num,arr[i])
        
    return lcm_num

"""
