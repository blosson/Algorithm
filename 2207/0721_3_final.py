# SWEA 2056. 연원일 달력 (pass 파일)

case_num = int(input())

date_list = []
for i in range(case_num):
    date = input()
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


