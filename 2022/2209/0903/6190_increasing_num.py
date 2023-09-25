for tc in range(1, int(input()) + 1):
    N = int(input())
    num_list = list(map(int, input().split()))

    check_num = []                                                          # i*j 곱한 값들을 담을 리스트
    for i in range(N):                      
        for j in range(i+1, N):
            check_num.append(num_list[i] * num_list[j])                     # 곱해서 리스트에 넣어주기

    final_check_list = []                                                   # 단조증가수면 넣어줄 리스트
    for i in range(len(check_num)):
        if list(str(check_num[i])) == sorted(list(str(check_num[i]))):      # 정렬한 리스트와 현재 리스트가 같으면 리스트에 추가
            final_check_list.append(check_num[i])
    
    if final_check_list:                                                    # 단조 증가수가 하나라도 있으면 최댓값 출력
        ans = max(final_check_list)                                           
    else:                                                                   # 없으면 -1 출력
        ans = -1
    
    print(f'#{tc} {ans}')
        
 