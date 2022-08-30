for tc in range(1, int(input()) + 1):
    
    N = int(input())
    numbers = list(map(int, input().split()))

    num_max = -float('inf')
    num_min = float('inf')
    for number in numbers:
        if number > num_max:
            num_max = number
        if number < num_min:
            num_min = number

    print(f'#{tc} {num_max - num_min}')

