N = int(input())
numbers = list(map(int, input().split()))


                                            # 1 - 증가 먼저 확인
cnt_increase = 1                            # 연속된 숫자 셀 변수
max_increase = 1                            # 최대 길이 변수
for i in range(1, N):
    if numbers[i] >= numbers[i-1]:          # 현재 인덱스의 값이 이전보다 같거나 크면 1증가
        cnt_increase += 1
        if max_increase < cnt_increase:     # 최댓값보다 크면 최댓값 업데이트
            max_increase = cnt_increase
    else:
        cnt_increase = 1

cnt_decrease = 1                            # 2 - 감소 확인
max_decrease = 1
for i in range(1, N):
    if numbers[i] <= numbers[i-1]:
        cnt_decrease += 1
        if max_decrease < cnt_decrease:
            max_decrease = cnt_decrease
    else:
        cnt_decrease = 1

ans = max(max_increase, max_decrease)       # 증가와 감소중 더 큰 값을 저장

if ans == 1:                                # 1로 끝나면 2로 바꿔줌 (정답이 최소 2이므로)
    ans = 2

print(ans)