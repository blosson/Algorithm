for tc in range(1, int(input()) + 1):
    N = int(input())
    num_list = list(map(int, input().split()))

    # print(num_list)
    check_num = []
    for i in range(N):
        for j in range(i+1, N):
            check_num.append(num_list[i] * num_list[j])
    # check_num = set(check_num)
    # check_num = list(check_num)
    # check_num = sorted(check_num)
    # # print(check_num)

    final_check_list = []
    for i in range(len(check_num)):
        if list(str(check_num[i])) == sorted(list(str(check_num[i]))):
            final_check_list.append(check_num[i])
    
    if final_check_list:
        ans = max(final_check_list)
    else:
        ans = -1
    
    print(f'#{tc} {ans}')
        
    # final_check_num = []
    # for i in range(len(check_num)):
    #     check_num_list = list(map(int, str(check_num[i])))
    #     sorted_check_num_list = sorted(check_num_list)
    #     if check_num_list == sorted_check_num_list:
    #         # print(check_num_list)
    #         for j in range(len(check_num_list)):
    #             check_num_list[j] = str(check_num_list[j])
    #         str_check_num = ''.join(check_num_list)
    #         int_check_num = int(str_check_num)
    #         final_check_num.append(int_check_num)

    # if final_check_num == False:
    #     ans = -1
    # else:
    #     ans = max(final_check_num)
    
    # print(f'#{tc} {ans}')