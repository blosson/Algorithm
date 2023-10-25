def solution(priorities, location):
    cnt = 1                         # 프로세스 진행 순서
    rank = [0] * len(priorities)    # idx별로 순서 담을 배열
    idx_list = []                   # idx와 우선순위 숫자 담을 배열
    
    for idx, priority in enumerate(priorities):     # idx, 우선순위 채우기
        idx_list.append([idx, priority])
    # print(idx_list)
    
    while idx_list:                 # 프로세스 마무리 될 때까지
        max_value = 0               # 우선순위 최대값 구하기
        for value in idx_list:
            if value[1] >= max_value:
                max_value = value[1]
        # print(max_value)
        
        process = idx_list.pop(0)   # 큐의 0번 인덱스 꺼내서 최우선순위인지 확인
        if process[1] == max_value: # 맞으면 순서 rank 배열에 넣어주고
            rank[process[0]] = cnt
            cnt += 1
            
        else:                       # 아니면 다시 배열 제일 뒤에 넣어줌
            idx_list.append(process)
            
        # print(idx_list)
        # print(rank) //
        
    answer = rank[location]
    return answer