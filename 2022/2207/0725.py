T = int(input()) # 테스트 케이스 입력

x = 1
while x <= T: # 테스트 케이스 개수만큼 반복
    while True: # N이 1이상 10이하 범위에 있는지 유효성 검사
        N = int(input())
        if 1 <= N <= 10:
            break
        else: 
            print('1 이상 10 이하의 정수를 입력하세요.')


    sum = 0
    for i in range(1, N+1): # 1부터 N까지 순환
        if i % 2 == 1: # 홀수이면 그대로 sum에 더함
            sum = sum + i
        else: # 짝수이면 음수 형태 sum에 더함
            sum = sum - i
    print(f'#{N} {sum}') # 출력
    x = x + 1 
