# <IDEA>
# - 최소 피로도 기준으로 내림차순 정렬해도 소모 피로도 때문에 정답이 아닐 수 있음
# - 소모 피로도 기준으로 내림차순 정렬해도 최소 피로도 때문에 정답이 아닐 수 있음
# - 결국 완전탐색 해야한다?
# 1. 던전의 개수에 맞게 순열을 이용해서 인덱스 정보를 담은 2차원 배열을 만듦
# 2. 2차원 배열을 순회하여 순서 확인 (최댓값 구하기)

from itertools import permutations

def solution(k, dungeons):
    # 던전의 개수 세서 개수만큼 배열 만들기
    cnt = len(dungeons)
    cnt_list = []
    for i in range(cnt):
        cnt_list.append(i)
    
    # 순열로 idx 순서 경우의 수 만들어 order_list에 넣어주기
    order_list = list(permutations(cnt_list, cnt))
    # print(order_list)
    
    # 최대 던전 탐험 횟수
    explore_cnt_max = 0
    # 순열 값들을 순회하여 최대 던점 탐험 갯수 계산
    for order in order_list:
        # print(order)
        energy = k
        explore_cnt = 0
        for idx in order:
            # print(idx)
            # 현재 체력이 최대 피로도 이상이면 탐험 + 1 하고 최댓값과 비교
            if energy >= dungeons[idx][0]:
                explore_cnt += 1
                energy -= dungeons[idx][1]
                
                if explore_cnt > explore_cnt_max:
                    explore_cnt_max = explore_cnt
                    
            # 더 이상 탐험할 수 없으면 다음 경우의 수로 넘어가기
            else:
                break
            
    return explore_cnt_max