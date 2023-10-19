#1 시간초과 버전 (배열)
def solution(participant, completion):
    answer = ''
    for person in participant:
        if person in completion:
            completion.remove(person)
        else:
            answer += person
            
    return answer


# 2 통과 버전 (딕셔너리)
# 배열삭제는 시간이 오래걸리는 데 반해 딕셔너리는 빨라서 통과된듯?
def solution(participant, completion):
    answer = ''
    # 딕셔너리 생성해서 각 이름이 몇번 나왔는지 기록
    running_dict = {}
    for person in participant:
        if person in running_dict:
            running_dict[person] += 1
        else:
            running_dict[person] = 1
    
    # 완주자 배열 순회하여 -1씩 해주기
    for person in completion:
        running_dict[person] -= 1
    
    # 1이 남아있는 사람이 있다면 그 사람이 완주하지 못한 선수
    for person in running_dict:
        if running_dict[person] == 1:
            answer += person
            break
              
    return answer



--------
# 3 괜찮아보이는 풀이
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for p, c in zip(participant, completion):
        if p != c:
            return p
    return participant[-1]


# 4
def solution(participant, completion):
    participant_set = set(participant)
    completion_set = set(completion)
    result = list(participant_set - completion_set)
    if result !=[]:
        return result[0]
    else:
        for c in completion:
            a=completion.count(c)
            b=participant.count(c)
            if(a != b):
                return c
    return None