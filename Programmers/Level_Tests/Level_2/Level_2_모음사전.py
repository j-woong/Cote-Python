"""
***로직***
1. 입력 변수
- word: 찾고자 하는 5글자 이하의 단어 문자열

2. 핵심 변수
- moeum_dict: 모음의 순서를 정렬해놓은 배열 사전 
- moeum: 모음을 담아놓은 배열

3. 핵심 로직
step1: 중복 순열 기반 문자 생성
- itertools 패키지의 product 라이브러리를 활용하여 1부터 6까지 차례대로 가지는 모음 단어 조합 생성
- 생성된 튜플 형태의 문자들을 join()함수를 이용하여 문자로 바꾸어 moeum_dict 배열에 누적 대입
step2: 사전식 정렬 구조
- 생성된 리스트를 sort() 함수를 이용하여 오름차순 정렬
step3: enumerate() 함수를 이용하여 인덱스와 함께 순회하며 주어진 문자 word와 같은 문자 char가 있다면 char의 인덱스에 +1 을 하여 반환함

4. 예외 처리
- 문자열 비교 우선순위 오류 제어
- AAAAE와 AAAE의 우선순위 차이로 인한 정렬 시 무엇이 더 앞서는지 파악해야 함
"""

from itertools import product
def solution(word):
    
    moeum_dict = []
    moeum = ['A','E','I','O','U']
    
    for cnt in range(1,6):
        for c in product(moeum, repeat=cnt):
            moeum_dict.append("".join(c))
            
    moeum_dict.sort()
    
    for idx, char in enumerate(moeum_dict):
        if word == char:
            return idx+1
    
    