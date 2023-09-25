T = int(input()) # 테스트 케이스 개수

# 기본적으로 while 문을 통한 나눗셈을 해서 소인수 분해를 진행
x = 1
while x <= T:
    N = int(input())
 
    a = 0
    while True:
        if N % 2 == 0:
            N = N / 2
            a += 1
        else:
            break

    N = N
    b = 0
    while True:
        if N % 3 == 0:
            N = N / 3
            b += 1
        else:
            break

    N = N
    c = 0
    while True:
        if N % 5 == 0:
            N = N / 5
            c += 1
        else:
            break

    N = N
    d = 0
    while True:
        if N % 7 == 0:
            N = N / 7
            d += 1
        else:
            break

    N = N
    e = 0
    while True:
        if N % 11 == 0:
            N = N / 11
            e += 1
        else:
            break

    print(f'#{x} {a} {b} {c} {d} {e}') # 출력
    x = x + 1