cm = int(input())

cnt = 0                # 막대기의 개수 (정답변수)
while cm > 0:          
    if cm % 2 == 0:    # 2로 나누어 떨어지면 2로 나누어줌
        cm //= 2
    else:              # 2로 나누어 떨어지지 않으면 막대기 기수 +1 해주고 2로 나눈 몫으로 재할당
        cnt += 1       
        cm //= 2

print(cnt)          
    