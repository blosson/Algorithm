import sys
sys.stdin = open('1959.txt', 'r')

for tc in range(1, int(input()) + 1):

    N, M = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))

    if N == M:                                                       # 같을 경우에는 한 번만 곱하면 됨
        multiplication_sum = 0
        for i in range(N):
            index_multiplication =  a_list[i] * b_list[i]
            multiplication_sum += index_multiplication
        ans = multiplication_sum

    elif N > M:
        multiplication_sum_max = -99999999999999999999999999999      # 일반 숫자는 한계가 있으므로 -float('inf') 이렇게 표현해주는 게 좋음
        for i in range(N - M + 1):                                   # abs(N-M) 이렇게 줬으면 아래 else:문에서 더 편했을듯
            multiplication_sum = 0
            for j in range(M):
                index_multiplication = a_list[j] * b_list[j]
                multiplication_sum += index_multiplication
            a_list.pop(0)                                            # 한 번 곱을 할 때마다 긴 쪽의 index 0을 pop해주면서 계속해서 비교
            if multiplication_sum > multiplication_sum_max:
                multiplication_sum_max = multiplication_sum
        ans = multiplication_sum_max

    else:
        multiplication_sum_max = -99999999999999999999999999999
        for i in range(M - N + 1):
            multiplication_sum = 0
            for j in range(N):
                index_multiplication = a_list[j] * b_list[j]
                multiplication_sum += index_multiplication
            b_list.pop(0)
            if multiplication_sum > multiplication_sum_max:
                multiplication_sum_max = multiplication_sum
        ans = multiplication_sum_max

    print(f'#{tc} {ans}')
