N = int(input())
numbers = list(map(int, input().split()))


                                            # 1 - 증가 먼저 확인
cnt_increase = 1                            # 연속된 숫자 셀 변수
max_result = 1                              # 최대 길이 변수
for i in range(1, N):
    if numbers[i] >= numbers[i-1]:          # 현재 인덱스의 값이 이전보다 같거나 크면 1증가
        cnt_increase += 1
        if max_result < cnt_increase:       # 최댓값보다 크면 최댓값 업데이트
            max_result = cnt_increase
    else:
        cnt_increase = 1

cnt_decrease = 1                            # 2 - 감소 확인
for i in range(1, N):
    if numbers[i] <= numbers[i-1]:
        cnt_decrease += 1
        if max_result < cnt_decrease:
            max_result = cnt_decrease
    else:
        cnt_decrease = 1

print(max_result)