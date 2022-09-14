for tc in range(1, int(input()) + 1):
    n, d = map(int, input().split())

    area = (d * 2) + 1              # 분무기의 범위
    if n % area == 0:               # n이 범위로 나누어 떨어지면
        ans = int(n / area)         # 몫만큼만 필요
    else:                           # 나머지가 발생하면
        ans = (n // area) + 1       # 몫 + 1만큼 분무기가 필요
    print(f'#{tc} {ans}')