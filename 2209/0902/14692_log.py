for tc in range(1, int(input()) + 1):   # 
    N = int(input())
    if N % 2 == 0:
        ans = 'Alice'
    else:
        ans = 'Bob'

    print(f'#{tc} {ans}')
        