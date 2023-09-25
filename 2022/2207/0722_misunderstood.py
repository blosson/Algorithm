# 문제 잘못 이해해서 풀었다.. 

while True:
    N = int(input())
    if 10 <= N <= 1000:
        break
    else:
        print('10이상 1000이하의 정수를 입력하세요.')


if N == 1000:
    print(N)
elif 100 <= N:
    if (N // 100) == 3 or (N // 100) == 6 or (N // 100) == 9: # 백의 자리에 3, 6, 9가 존재할 때
        N_str = str(N) # int -> str 변경 (추출하기 위해)
        N_str_2 = int(N_str[1:3])   # 뒤의 2자리 추출 
        if (N_str_2 // 10) == 3 or (N_str_2 // 10) == 6 or (N_str_2 // 10) == 9:
            if (N % 10) == 3 or (N % 10) == 6 or (N % 10) == 9: #333
                print('---')
            else:   #331
                print('--')
        else: 
            if (N % 10) == 3 or (N % 10) == 6 or (N % 10) == 9: #313
                print('--')
            else:   #311
                print('-')      

    else: # 백의 자리에 3, 6, 9가 없을 때
        N_str = str(N)
        N_str_2 = int(N_str[1:3])
        if (N_str_2 // 10) == 3 or (N_str_2 // 10) == 6 or (N_str_2 // 10) == 9:
            if (N % 10) == 3 or (N % 10) == 6 or (N % 10) == 9: #133
                print('--')
            else:   #131
                print('-')
        else: 
            if (N % 10) == 3 or (N % 10) == 6 or (N % 10) == 9: #113
                print('-')
            else:   #111
                print(N)  

elif N < 100:
    if (N // 10) == 3 or (N // 10) == 6 or (N // 10) == 9:
        if (N % 10) == 3 or (N % 10) == 6 or (N % 10) == 9: #33
            print('--')
        else:   #31
            print('-')
    else: 
        if (N % 10) == 3 or (N % 10) == 6 or (N % 10) == 9: #13
            print('-')
        else:   #11
            print(N)
    
        
