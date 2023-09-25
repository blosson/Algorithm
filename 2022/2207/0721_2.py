# SWEA 2056. 연원일 달력

case_num = int(input('테스트 케이스 개수를 입력하세요. : '))

date_list = []
for i in range(case_num):
    date = input('8자리 날짜를 입력하세요. : ')
    date_list.append(date)

n = 1
while n <= case_num: 
    
    month = date_list[n-1][4:6] 
    day = date_list[n-1][6:8] 

    if (len(date_list[n-1]) == 8) and (1 <= int(month) <= 12): 
    
        if (int(month) % 2 == 1) or (int(month) == 8): 
            if 1 <= int(day) <= 31:
                print(f'#{n} {date_list[n-1][0:4]}/{date_list[n-1][4:6]}/{date_list[n-1][6:8]}')
            else:
                print(f'#{n} -1')

        elif (int(month) % 2 == 1) and (int(month) != 8): 
            if 1 <= int(day) <= 30:
                print(f'#{n} {date_list[n-1][0:4]}/{date_list[n-1][4:6]}/{date_list[n-1][6:8]}')
            else:
                print(f'#{n} -1')

        else: 
            if 1 <= int(day) <= 28:
                print(f'#{n} {date_list[n-1][0:4]}/{date_list[n-1][4:6]}/{date_list[n-1][6:8]}')
            else:
                print(f'#{n} -1')
    else: 
        print(f'#{n} -1')

    n = n + 1


# 1. 숫자에도 리스트 자리값이 있어서 추출이 쉬우면 좋은데 문자열만 가능해서 어떻게 하면 좋을지 모르겠다.

# 2. 0***로 시작하는 년도에 대해서는 어떻게 작동시킬 수 있을지 모르겠다. -> 처음 입력받을 때 int로 안 받으면 자동으로 str처리 되니까 이렇게 하면 가능하다!

# 3. 입력-출력처럼 한 번에 가지런하게 나오게는 못하나..'''