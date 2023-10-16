# <IDEA>
# - 광물을 순서대로 캐야하기 때문에 정렬이 의미가 없음.
# - 결국 완전 탐색을 해야하고 그 안에서 백트래킹?을 해서 중간 중간 걸러낼 수 밖에 없을듯 (input이 크지 않아서 괜찮을 것 같음)
# 1. minerals의 길이를 세고 곡괭이의 개수를 세서 최대 몇개의 곡괭이를 꺼낼 수 있는지 계산
# 2. 곡괭이를 하나씩 순회해서 꺼냄
#     - 이걸 어떻게 하는지가 문제임. 어떻게 하면 순서대로 빠짐없이 순회할 수 있을까?
#     - 순열이 떠오르는데 내가 구현할 수는 없
# 3. minerals를 순회하면서 최솟값을 찾음
    
#     1) 이미 min 이상이면 break
#     2) 곡괭이를 다 사용하면 그 값을 min과 확인
#     3) 광물을 끝까지 캤으면 그 값을 min과 확인


#1 (시간초과)

from itertools import permutations

def solution(picks, minerals):
    # 현재 곡괭이와 광물 인덱스를 리스트에 저장 (0: 다이아몬드, 1: 철, 2: 돌)
    fatigue = [[1, 1, 1], [5, 1, 1], [25, 5, 1]]
    
    # 사용 가능한 곡괭이의 개수 계산
    if len(minerals) % 5 == 0:
        pickax_num = len(minerals) // 5
    else:
        pickax_num = (len(minerals) // 5) + 1
    # 곡괭이가 모자라서 광물을 다 캘 수 없을 경우 곡괭이 개수 조정
    if sum(picks) < pickax_num:
        pickax_num = sum(picks)
    
    # 곡괭이 종류들을 new_picks 배열에 담아줌
    new_picks = []
    for idx,i in enumerate(picks):
        # print(idx, i)
        for _ in range(i):
            new_picks.append(idx)
    # print(new_picks)
        
    # 순열 사용해서 순회할 곡괭이 리스트 생성
    pickax_list = list(set(list(permutations(new_picks, pickax_num))))
    # print(pickax_list)

    min_fatigue = 99999999999999999
    for pickax in pickax_list:
        fatigue_cnt = 0
        for i in range(len(minerals)):
            idx = i // 5
            if pickax_num > idx:
                if minerals[i] == 'diamond':
                    fatigue_cnt += fatigue[pickax[idx]][0]
                elif minerals[i] == 'iron':
                    fatigue_cnt += fatigue[pickax[idx]][1]
                else:
                    fatigue_cnt += fatigue[pickax[idx]][2]
                # print(pickax[idx], minerals[i], fatigue_cnt)
                
            # 광물을 캐다가 피로도가 최소값 이상이면 탐색 종료
            if fatigue_cnt >= min_fatigue:
                break
                
        # 피로도가 현재까지의 최소 피로도보다 작으면 최소 피로도 변경
        if fatigue_cnt < min_fatigue:
            min_fatigue = fatigue_cnt
    
    return min_fatigue