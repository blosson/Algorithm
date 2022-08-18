for tc in range(1, int(input()) + 1):

    str1 = input() # pattern
    str2 = input() # target

    pure_str1 = list(set(str1))         # set로 중복 글자 제거
    max_cnt = 0                         
    for j in range(len(pure_str1)):     # pattern 먼저 반복
        cnt = 0
        for i in range(len(str2)):
            if pure_str1[j] == str2[i]:
                cnt += 1
        if cnt > max_cnt:
            max_cnt = cnt

    print(f'#{tc} {max_cnt}')

