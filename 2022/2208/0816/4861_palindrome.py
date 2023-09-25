import sys
sys.stdin = open('4861.txt', 'r')

T = int(input())
for tc in range(1, T+1):

    N, M = list(map(int, input().split()))
    letters = [list(input()) for _ in range(N)]

    for i in range(N):                                # case row
        for j in range(N-M+1):                        # 길이가 M인 경우 총 0 ~ N-M개 순회 가능
            test_list = letters[i][j:j+M]             # 길이가 M인 test_list 생성  
            if test_list == test_list[::-1]:          
                ans_row = ''.join(test_list)
                print(f'#{tc} {ans_row}')

    for l in range(N):                                # case column
        for k in range(N-M+1):
            cnt = 0                                 
            test_list2 = []                                                     
            while cnt < M:      
                test_list2.append(letters[k+cnt][l])  # while문을 활용하여 길이가 M인 list 생성 (column 확인 위해)
                cnt += 1                        
           
            if test_list2 == test_list2[::-1]:
                ans_col = ''.join(test_list2)
                print(f'#{tc} {ans_col}')
            

                    
                      