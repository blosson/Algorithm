# 1 시간 초과 버전

def solution(id_list, report, k):
    answer = []
    # 신고자 - 신고대상을 담을 딕셔너리 생성
    report_dict = {}
    for id in id_list:
        report_dict[id] = []
    
    # ' '기준으로 신고자 - 신고대상 나눈 후, 중복값이 들어가지 않게 딕셔너리에 넣어줌
    for s in report:
        reporter, villain = s.split(' ')[0], s.split(' ')[1]
        
        if not villain in report_dict[reporter]:
            report_dict[reporter].append(villain)
    
    # 신고 횟수 도달로 정지된 아이디를 리스트에 담아줌
    banned_list = []
    for id in report_dict:
        cnt = 0
        for value in report_dict.values():
            if id in value:
                cnt += 1
        if cnt >= k:
            banned_list.append(id)
    
    # report_dict의 신고자가 신고한 대상이 몇개나 정지당했는지 계산 후 정답에 추가
    for id in report_dict:
        cnt = 0
        for banned_id in banned_list:
            if banned_id in report_dict[id]:
                cnt += 1
        answer.append(cnt)
    
    return answer

# 2 통과 버전
def solution(id_list, report, k):
    answer = []
    report_dict = {}
    for id in id_list:
        report_dict[id] = []
    
    # 중복 신고를 없애기 위해 set 사용
    report = list(set(report)
    for s in report:
        reporter, villain = s.split(' ')[0], s.split(' ')[1]
        # 이미 중복 제거를 했으니 if문 없이 바로 key-value 형태로 넣어줌
        report_dict[reporter].append(villain)
        
    banned_list = []
    
    for id in report_dict:
        cnt = 0
        for value in report_dict.values():
            if id in value:
                cnt += 1
        if cnt >= k:
            banned_list.append(id)
    
    for id in report_dict:
        cnt = 0
        for banned_id in banned_list:
            if banned_id in report_dict[id]:
                cnt += 1
        answer.append(cnt)
    
    return answer


-------
# 찾아본 깔끔한 풀이
def solution(id_list, report, k):
    answer = [0] * len(id_list)    
    reports = {x : 0 for x in id_list}

    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer