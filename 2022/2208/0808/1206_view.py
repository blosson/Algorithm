
for n in range(1, 11): # 10개의 테스트 케이스 반복
    test_case = int(input()) # 가로 길이
    floors = list(map(int, input().split())) # 빌딩들의 층수 입력

    numbers = 0 # 조망권이 있는 세대 수 
    for i in range(2, (len(floors) - 2)): # 양쪽 2세대 씩 빼기
        check1 = floors[i] - floors[i-2] # 양쪽 2값씩 비교
        check2 = floors[i] - floors[i-1]
        check3 = floors[i] - floors[i+1]
        check4 = floors[i] - floors[i+2]
        if check1 > 0 and check2 > 0 and check3 > 0 and check4 > 0:
            view_point = min(check1, check2, check3, check4) # 조망 가능 세대 수
            numbers = numbers + view_point
            
    print(f'#{n} {numbers}')
        