# SWEA 2056. 연원일 달력

case_num = int(input('테스트 케이스 개수를 입력하세요. : '))

n = 1

while n <= case_num: 
    date = input('8자리 날짜를 입력하세요. : ')
    month = date[4:6] # 월을 검사하기 위해 설정한 변수
    day = date[6:8] # 일을 검사하기 위해 설정한 변수
    if (len(date) == 8) and (1 <= int(month) <= 12): # 8자리 맞는지, 달이 1~12가 맞는지 묻는 if 문
    
        if (int(month) % 2 == 1) or (int(month) == 8): # 31일까지 있는 달을검사하는 if문
            if 1 <= int(day) <= 31:
                print(f'#{n} {date[0:4]}/{date[4:6]}/{date[6:8]}')
            else:
                print(f'#{n} -1')
        elif (int(month) % 2 == 1) and (int(month) != 8): # 30일까지 있는 달을검사하는 if문
            if 1 <= int(day) <= 30:
                print(f'#{n} {date[0:4]}/{date[4:6]}/{date[6:8]}')
            else:
                print(f'#{n} -1')
        else: # 2월을 검사하는 if문
            if 1 <= int(day) <= 28:
                print(f'#{n} {date[0:4]}/{date[4:6]}/{date[6:8]}')
            else:
                print(f'#{n} -1')
    else: # 8자리 아닐경우 or 월이 1~12 범위에 있지 않을 경우
        print(f'#{n} -1')

    n = n + 1


# 1. 숫자에도 리스트 자리값이 있어서 추출이 쉬우면 좋은데 문자열만 가능해서 어떻게 하면 좋을지 모르겠다.

# 2. 0***로 시작하는 년도에 대해서는 어떻게 작동시킬 수 있을지 모르겠다. -> 처음 입력받을 때 int로 안 받으면 자동으로 str처리 되니까 이렇게 하면 가능하다!

# 3. 입력-출력처럼 한 번에 가지런하게 나오게는 못하나..