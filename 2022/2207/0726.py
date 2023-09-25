T = int(input()) # 테스트 케이스 개수

# 기본적으로 while 문을 통한 나눗셈을 해서 소인수 분해를 진행
x = 1
while x <= T:
    N = int(input())
    N_2 = N # 소수별로 N값이 변하는 걸 방지하기 위해 새로운 변수 설정
    a = 0
    while True:
        if N_2 % 2 == 0:
            N_2 = N_2 / 2
            a += 1
        else:
            break

    N_3 = N
    b = 0
    while True:
        if N_3 % 3 == 0:
            N_3 = N_3 / 3
            b += 1
        else:
            break

    N_5 = N
    c = 0
    while True:
        if N_5 % 5 == 0:
            N_5 = N_5 / 5
            c += 1
        else:
            break

    N_7 = N
    d = 0
    while True:
        if N_7 % 7 == 0:
            N_7 = N_7 / 7
            d += 1
        else:
            break
        
    N_11 = N
    e = 0
    while True:
        if N_11 % 11 == 0:
            N_11 = N_11 / 11
            e += 1
        else:
            break

    print(f'#{x} {a} {b} {c} {d} {e}') # 출력
    x = x + 1


