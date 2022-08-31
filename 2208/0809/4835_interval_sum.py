
for tc in range(1, int(input()) + 1):

    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    check_list = [0] * (N - M + 1)
    for i in range(N-M+1):
        check_list[i] = sum(numbers[i:i+M])

    print(f'#{tc} {max(check_list) - min(check_list)}')
    

