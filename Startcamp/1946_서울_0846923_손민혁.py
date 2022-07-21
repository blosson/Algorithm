T = int(input())
for t in range(1, T+1): 
    N = int(input())
    document = ''
    for j in range(N):
        Ci, Ki = input().split()
        Ki = int(Ki)
        while True:
            if Ki <= 0:
                break
            document += Ci
            Ki -= 1

    print('#{}'.format(t))
    count = 1
    for c in document:
        print(c, end='')
        if count % 10 == 0:
            print()
        count += 1
    print()

# 이 문제는 구글링을 통해 봐도 잘 이해가 되지 않습니다..