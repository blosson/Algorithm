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
            for j in range(i, M + i):                               # range(M)이 아니라 range(i, M + i)를 해주고 for문이 끝날 때마다
                index_multiplication = a_list[j] * b_list[j]        # 짧은 쪽 index 0에 [0]을 추가해주는 IDEA!
                multiplication_sum += index_multiplication
            b_list = [0] + b_list                                   # [0] 리스트 index 0에 추가
            if multiplication_sum > multiplication_sum_max:
                multiplication_sum_max = multiplication_sum
        ans = multiplication_sum_max

    else:
        multiplication_sum_max = -99999999999999999999999999999
        for i in range(M - N + 1):
            multiplication_sum = 0
            for j in range(i, N + i):
                index_multiplication = a_list[j] * b_list[j]
                multiplication_sum += index_multiplication
            a_list = [0] + a_list
            if multiplication_sum > multiplication_sum_max:
                multiplication_sum_max = multiplication_sum
        ans = multiplication_sum_max
    
    print(f'#{tc} {ans}')
 

