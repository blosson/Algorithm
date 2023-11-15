def solution(lottos, win_nums):
    # 순위 딕셔너리 생성, 알 수 없는 번호 개수 count
    winning_rank = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6 }
    zero_cnt = lottos.count(0)
    
    # 0를 제외한 숫자 중 당첨 번호와 일치하는 개수 계산
    cnt = 0
    for i in lottos:
        if i in win_nums:
            cnt += 1
    
    # 최대, 최소 일치 개수 구하기
    max_cnt = cnt + zero_cnt
    min_cnt = cnt
    
    answer = [winning_rank[max_cnt], winning_rank[min_cnt]]
    
    return answer