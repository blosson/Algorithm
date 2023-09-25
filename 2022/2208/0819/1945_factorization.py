'''
몇번이나 인수분해가 진행될지 모르므로 while을 떠올리는 게 핵심

'''
for tc in range(1, int(input()) + 1):
    number = int(input())

    a = b = c = d = e = 0                                   # 초기값 설정
    abcde_list = [a, b, c, d, e]                            # abcde값 담을 리스트
    factorization_list = [2, 3, 5, 7, 11]                   # 나눌 리스트

    for i in range(len(factorization_list)):                # 각 숫자별로 for문 돌려서
        while True:
            if number % factorization_list[i] == 0:         # 해당값으로 나누어지면
                abcde_list[i] += 1                          # abcde 값을 증가시키고
                number = number / factorization_list[i]     # number를 나누어준다
            else:
                break                                       # 더이상 나누어지지 않으면 다음 숫자로 이동
    
    print(f'#{tc}', *abcde_list)                            # print 구분해주어 출력 형식 맞춰줌