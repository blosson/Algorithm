for tc in range(1, int(input()) + 1):

    N, M  = map(int, input().split())
    numbers = list(map(int, input().split()))

    for _ in range(M % N):                  # 그냥 M만 해도 되지만 어차피 반복되므로 시간절약을 위해 M % N으로 넣어줌 
        numbers.append(numbers.pop(0))

    print(f'#{tc} {numbers[0]}')

