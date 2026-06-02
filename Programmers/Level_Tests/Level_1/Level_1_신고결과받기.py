"""
***로직***
1. 입력 변수
- id_list: 유저 아이디를 담은 배열
- report: [신고당한 유저,신고한 유저] 배열을 담은 배열
- k: 게시판 이용 정지 횟수
2. 핵심 변수
- reported_list: {유저id: [신고한 유저들]} 을 담은 딕셔너리
- count_list: {유저id: 신고당한 횟수} 를 담은딕셔너리
- answer:  유저가 신고한 사람이 k번 이상 신고당했을 때 받는 메일 배열
3. 핵심 로직
step1: 딕셔너리 생성
- id_list 배열을 순회하며 횟수와 신고한 유저를 담는 딕셔너리를 각각 생성
step2: 신고한 유저와 신고당한 횟수 카운트
- report 배열을 순회하며 공백 기준으로 분리하여 0번째를 usid로, 첫번째(usid가 신고한 id)를 value값으로 하는 리스트에 추가
- 벨류값에 같은 유저가 없다면 횟수 +1 처리
step3: 메일 카운트
- 신고한 유저 딕셔너리의 키값을 기준으로 순회하며 신고한 유저가 k번이상 신고당했다면 신고한 유저의 메일 +1 처리
4. 예외 처리
- 한 유저가 같은 유저를 여러번 신고해도 횟수를 1로 처리하기위해 조건문을 추가
- 한번도 신고 당하지않은 유저가 있기때문에 count_list의 초기 딕셔너리 값을 0으로 지정
- 
"""
def solution(id_list, report, k):
    reported_list = {}
    count_list = {}
    for usid in id_list:
        count_list[usid] = 0
        reported_list[usid] = []
    
    for r in report:
        usid, report_usid = r.split()
        
        if report_usid not in reported_list[usid]:
            reported_list[usid].append(report_usid)
            count_list[report_usid] += 1
        
    answer = []
    for report_usid in reported_list.values():
        cnt = 0
        for p in report_usid:
            if count_list[p] >= k:
                cnt += 1
        answer.append(cnt)
        
    return answer
    