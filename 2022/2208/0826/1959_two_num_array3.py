import sys
sys.stdin = open('1959.txt', 'r')

for tc in range(1, int(input()) + 1):

    N, M = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))

    if N == M:                                                      # 같을 경우에는 한 번만 곱하면 됨
        multiplication_sum = 0
        for i in range(N):
            index_multiplication =  a_list[i] * b_list[i]       
            multiplication_sum += index_multiplication
        ans = multiplication_sum

    elif N > M:
        multiplication_sum_max = -99999999999999999999999999999     # -float('inf') 사용하기!
        for i in range(N - M + 1):                                  # abs 사용하면 더 편함
            multiplication_sum = 0
            for j in range(M):                             
                index_multiplication = a_list[j+i] * b_list[j]      # 긴 리스트 index에만 j가 아닌 j+i를 넣어주는 아이디어! 
            if multiplication_sum > multiplication_sum_max:
                multiplication_sum_max = multiplication_sum
        ans = multiplication_sum_max

    else:
        multiplication_sum_max = -99999999999999999999999999999
        for i in range(M - N + 1):
            multiplication_sum = 0
            for j in range(N):
                index_multiplication = a_list[j] * b_list[j+i]
                multiplication_sum += index_multiplication
            if multiplication_sum > multiplication_sum_max:
                multiplication_sum_max = multiplication_sum
        ans = multiplication_sum_max
    
    print(f'#{tc} {ans}')
 

