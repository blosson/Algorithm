for tc in range(1, int(input()) + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    ans = max(numbers) - min(numbers)

    print(f'#{tc} {ans}')