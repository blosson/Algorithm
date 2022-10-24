# 더 따뜻한 날씨를 위해서는 며칠을 더 기다려야 하는지를 출력하라.
tem = list(map(int, input().split()))
days = []                               # 정답 출력할 리스트

days_num = len(tem)
for i in range(days_num):
    cnt = 0                             
    found = 'no'                        # 더 따뜻한 날씨가 있는지 없는지
    for j in range(i+1, days_num):
        if tem[j] > tem[i]:             # 인덱스 j의 날씨가 현재날씨보다 더 따뜻하면
            cnt += 1                    # 날짜 +1
            found = 'yes'               # 찾았다.
            days.append(cnt)            # 리스트에 추가
            break                       # 두 번째 for문 종료

        else:                           # 더 따뜻하지 않으면
            cnt += 1                    # 날짜 +1
            found = 'no'                

    if found == 'no':                   # 마지막 날짜까지 봤는데 더 따뜻하지 않으면
        cnt = 0                         # cnt를 0으로 변경하고 리스트에 추가
        days.append(cnt)                

print(days)
    
    
