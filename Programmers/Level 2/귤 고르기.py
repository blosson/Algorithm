# <IDEA>
# 1. 현재 list의 길이 - k 만큼 리스트 안의 요소를 제거해줘야 함.
# 2. 각 요소들을 딕셔너리에 담아서 cnt를 세줌
# 3. 딕셔너리 순회하면서 가장 개수가 작은 것들을 cnt -1해
# 4. 딕셔너리를 다시 순회하면서 cnt가 1이상인 것만 세어 정답 출력

# <복습한 것들>
# 1. lambda 함수 value 정렬
# 2. tuple 자료형 (불변형)

def solution(k, tangerine):
    t_len = len(tangerine)
    # 제거할 귤의 개수
    removal_num = t_len - k
    
    # 귤의 크기, 개수를 key-value로 하는 딕셔너리 생성
    t_dict = {}
    for t in tangerine:
        if t not in t_dict:
            t_dict[t] = 1
        else:
            t_dict[t] += 1
    # print(t_dict)
    
    # cnt가 적은 순서대로 정렬 (튜플이 담긴 리스트)
    t_list = sorted(t_dict.items(), key=lambda x : x[1])
    
    # 튜플은 값 변경이 안돼서 다시 딕셔너리로 만들어줌
    t_dict = {}
    for t in t_list:
        t_dict[t[0]] = t[1]
    # print(t_dict)
    
    
    # 갯수가 작은 귤의 크기부터 -해줌
    for t in t_dict:
        if removal_num == 0:
            break
        while removal_num:
            if t_dict[t] >= 1:
                t_dict[t] -= 1
                removal_num -= 1
                
            else:
                break
    # print(t_dict)
    
    # 다시 딕셔너리 순회하면서 남아있는 귤의 크기면 +1
    answer = 0
    for t in t_dict:
        if t_dict[t] >= 1:
            answer += 1
    
    return answer