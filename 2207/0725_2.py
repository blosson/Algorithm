T = int(input()) # 테스트 케이스 입력

x = 1
list = []
while x <= T: # 테스트 케이스 개수만큼 반복
    while True: # N이 1이상 10이하 범위에 있는지 유효성 검사
        N = int(input())
        if 1 <= N <= 10:
            break
        else: 
            print('1 이상 10 이하의 정수를 입력하세요.')
    list.append(N)
    x = x + 1

# 여기까지 T 개수만큼 N값을 입력 받아서 list에 저장하는 역할
for k in list:
    sum = 0
    for i in range(1, k+1): # 1부터 k까지 순환
        if i % 2 == 1: # 홀수이면 그대로 sum에 더함
            sum = sum + i
        else: # 짝수이면 음수 형태 sum에 더함
            sum = sum - i
    print(f'#{k} {sum}') # 출력

