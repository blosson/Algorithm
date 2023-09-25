test_case = int(input())

n = 0
for n in range(test_case):
    days = int(input()) # 날짜수
    daily_price = list(map(int, input().split())) # 날짜별가격

    earning_sum = 0 # 수익
    for i in range(len(daily_price)): # 날짜별 가격 순회
        if daily_price[i] <= max(daily_price[i:]): # 자기 자신과 자기 자신 이후에 있는 리스트 값 중에서 최댓값 비교
            earning_sum = earning_sum + (max(daily_price[i:]) - daily_price[i]) # 수익 더해주기

    print(f'#{n+1} {earning_sum}')

        
