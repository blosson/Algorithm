import sys
sys.stdin = open('1208.txt', 'r')


for tc in range(10):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)] # list comprehension

    comparison_list = [] # 4가지 요소를 담을 리스트
    # 행의 합
    row_sum_max = 0          
    for i in range(100):
        sum_row = 0
        for j in range(100):
            sum_row += arr[i][j]
        if row_sum_max < sum_row:
            row_sum_max = sum_row

    comparison_list.append(row_sum_max)

    # 열의 합
    col_sum_max = 0  
    for j in range(100):
        sum_col = 0
        for i in range(100):
            sum_col += arr[i][j]
        if col_sum_max < sum_col:
            col_sum_max = sum_col

    comparison_list.append(col_sum_max)

    # (N, N) 대각선
    diagonal_sum = 0
    for i in range(100):
        diagonal_sum += arr[i][i] # i == j 이므로

    comparison_list.append(diagonal_sum)


    # 반대 대각선
    reverse_diagonal_sum = 0
    for i in range(100):
        for j in range(100):
            if i + j == 99: # 반대 대각선의 행과 열 index 규칙을 찾아줬음
                reverse_diagonal_sum += arr[i][j]

    comparison_list.append(reverse_diagonal_sum)

    ans_max = 0
    for i in comparison_list: # 행, 열, 두 대각선 중 최댓값 구하기
        if i > ans_max:
            ans_max = i

    print(f'#{tc+1} {ans_max}')

    
