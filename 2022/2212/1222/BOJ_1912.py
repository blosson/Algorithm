# Brute Force 시간초과 버전 (이거 어떻게 줄임..?)

N = int(input())
num_list = list(map(int, input().split()))

sum_max = float('-inf')                         # 임의의 무한 음수
for i in range(1, N+1):                         # 부분합은 1부터 N까지의 길이를 가질 수 있음 (부분합의 길이)
    for j in range(N+1-i):                      # 부분합의 길이에 따라 슬라이싱되는 부분의 갯수
        if sum(num_list[j:j+i]) > sum_max:      # 각 부분합이 최댓값보다 크면 최댓값을 갱신
            sum_max = sum(num_list[j:j+i])

print(sum_max)                                  # 최댓값 출력
