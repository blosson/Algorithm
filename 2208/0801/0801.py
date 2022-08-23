
test_case = int(input()) # 테스트 케이스

for case in range(test_case): # 테스트 케이스 반복
    day = input() # 요일 입력 (string)
    days_list = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'] # 요일 리스트

    for num in range(7): # 리스트의 자리값을 차례로 출력하기 위한 for문
        if day == days_list[num]: # 입력값과 리스트의 요소가 같으면
            if day == 'SUN': # SUN일 경우
                print(f'#{case + 1} 7') # 7을 출력
            else:
                print(f'#{case + 1} {6-num}') # 나머지는 (6-자신의 리스트 위치값) 출력
        
        
