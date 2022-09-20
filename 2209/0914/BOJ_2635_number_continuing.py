# BOJ_2635_수 이어가기

n = int(input())

if n == 1:                                  # 1일 때는 한 가지 경우의 수밖에 없으므로 그냥 하드코딩으로 출력
    max_cnt = 4
    max_list = [1, 1, 0, 1]

                                            # 기본적으로 1을 제외한 모든 수는 n/2보다 작은 수가 2번째로 오면 4번째는 반드시 음수가 오게 되고 max가 3이 됨
                                            # 그러나 n이 2번째로 오면 'n n 0 n 음수'로 최소 max가 4가 되기 때문에 n/2 미만의 수는 고려할 필요가 없음

elif n % 2 == 0:                            # 짝수일 때 
    max_cnt = 2                             # 1, 2번째 수는 무조건 있으므로 기본 max_cnt = 2   
    max_list = []
    for i in range(n//2, n):                # 2로 나누어 떨어지므로 range(n//2)로 시작

        cnt = 2                             # 1, 2번째 수는 무조건 있으므로 기본 cnt = 2
        check_list = [n, i]                 # 가장 처음 수 
        temp_n = n                          # n과 i 헷갈리지 않게 temp_n, temp_i라는 변수 생성
        temp_i = i

        while temp_i >= 0:                  # 다음 수가 음수가 아니면

            just = temp_i                   # temp_i 잃어버리지 않기 위한 임시변수
            temp_i = temp_n - temp_i        # 다음 숫자
            temp_n = just                   # 기존 temp_i를 temp_n에 넣어줌 (while문 반복을 위해)

            if temp_i < 0:                  # 다음 숫자가 음수면 break
                break

            check_list.append(temp_i)       # 다음 숫자가 음수가 아니라면 출력할 리스트에 넣어줌
            cnt += 1                        
            
            if cnt > max_cnt:               # max 비교
                max_cnt = cnt
                max_list = check_list       # 기존 리스트에 이렇게 입힐 수도 있구나.. (몰랐음)

else:                                       # 홀수일 때 (3의 경우 3//2가 1이므로 +1을 해주어야 3/2보다 큰 값이 될 수 있음)
    max_cnt = 2
    max_list = []
    for i in range(n//2 + 1, n):            # 위의 이유로 range (n//2 + 1)로 시작

        cnt = 2
        check_list = [n, i]
        temp_n = n
        temp_i = i

        while temp_i >= 0:

            just = temp_i
            temp_i = temp_n - temp_i
            temp_n = just

            if temp_i < 0:
                break

            check_list.append(temp_i)
            cnt += 1
            
            if cnt > max_cnt:
                max_cnt = cnt
                max_list = check_list

print(max_cnt)
print(*max_list)