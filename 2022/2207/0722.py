while True:
    N = int(input())
    if 10 <= N <= 1000:
        break
    else:
        print('10이상 1000이하의 정수를 입력하세요.')


for i in range(1, N+1):
    if N == 1000:
        print(i)
    elif 100 <= i:
        if (i // 100) == 3 or (i // 100) == 6 or (i // 100) == 9: # 백의 자리에 3, 6, 9가 존재할 때
            i_str = str(N) # int -> str 변경 (추출하기 위해)
            i_str_2 = int(i_str[1:3])   # 뒤의 2자리 추출 
            if (i_str_2 // 10) == 3 or (i_str_2 // 10) == 6 or (i_str_2 // 10) == 9:
                if (i % 10) == 3 or (i % 10) == 6 or (i % 10) == 9: #333
                    print('---', end = ' ')
                else:   #331
                    print('--', end = ' ')
            else: 
                if (i % 10) == 3 or (i % 10) == 6 or (i % 10) == 9: #313
                    print('--', end = ' ')
                else:   #311
                    print('-', end = ' ')      

        else: # 백의 자리에 3, 6, 9가 없을 때
            i_str = str(i)
            i_str_2 = int(i_str[1:3])
            if (i_str_2 // 10) == 3 or (i_str_2 // 10) == 6 or (i_str_2 // 10) == 9:
                if (i % 10) == 3 or (i % 10) == 6 or (i % 10) == 9: #133
                    print('--', end = ' ')
                else:   #131
                    print('-', end = ' ')
            else: 
                if (i % 10) == 3 or (i % 10) == 6 or (i % 10) == 9: #113
                    print('-', end = ' ')
                else:   #111
                    print(i, end = ' ')  

    else:
        if (i // 10) == 3 or (i // 10) == 6 or (i // 10) == 9:
            if (i % 10) == 3 or (i % 10) == 6 or (i % 10) == 9: #33
                print('--', end = ' ')
            else:   #31
                print('-', end = ' ')
        else: 
            if (i % 10) == 3 or (i % 10) == 6 or (i % 10) == 9: #13
                print('-', end = ' ')
            else:   #11
                print(i, end = ' ')  

        