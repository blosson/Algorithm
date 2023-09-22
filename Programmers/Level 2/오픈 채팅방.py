# <IDEA>
# - replace로 이름을 함부로 바꿔버리면 다른 중복된 닉네임까지 변경되므로 다른 방법을 찾아야 함
# - id를 key, 닉네임을 value로 하는 딕셔너리를 생성해서 바꿔줌, for문을 두 번 돌려야함
# - result 창에 value값을 출력

def solution(record):
    result = []
    user_dict = {}
    # 최종 변경 닉네임 정보 입력을 위한 for문
    for infos in record:
        # split 후 정보 종류와 아이디를 먼저 변수 설정 (퇴장인 경우에는 2번 idx가 없기 때문)
        info = infos.split(' ')
        info_type, user_id = info[0], info[1]
        
        # id 정보가 user_dict에 없을 시 추가
        if user_id not in user_dict:
            user_dict[user_id] = info[2]
        # print(user_dict)
        
        # id 정보가 있지만 쟁비장시 닉네임이 바뀌므로 value 변경
        else:
            if info_type == 'Enter':
                nickname = info[2]
                user_dict[user_id] = nickname
    
        # 닉에미 변경 시 value 변경
        if info_type == 'Change':
            nickname = info[2]
            user_dict[user_id] = nickname
    
    # result 출력을 위한 for문 (바뀔 닉네임으로 출력)
    for infos in record:
        info = infos.split(' ')
        info_type, user_id = info[0], info[1]
        
        # 입장, 퇴장 시 문구 출력
        if info_type == 'Enter':
            result.append(user_dict[user_id] + "님이 들어왔습니다.")
            continue
        if info_type == 'Leave':
            result.append(user_dict[user_id] + "님이 나갔습니다.")
    
    return result



----
#2 깔끔한 풀이
def solution(record):
    answer = []
    namespace = {}
    printer = {'Enter':'님이 들어왔습니다.', 'Leave':'님이 나갔습니다.'}
    for r in record:
        rr = r.split(' ')
        if rr[0] in ['Enter', 'Change']:
            namespace[rr[1]] = rr[2]

    for r in record:
        if r.split(' ')[0] != 'Change':
            answer.append(namespace[r.split(' ')[1]] + printer[r.split(' ')[0]])

    return answer