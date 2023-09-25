N = int(input())
numbers = [list(map(int, input().split())) for _ in range(N)]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

abs_sum_all = 0
for i in range(N):
    for j in range(N):
        abs_sum = 0
        for k in range(4):
         ni = i + di[k]
         nj = j + dj[k]
         if 0 <= ni < N and 0 <= nj < N:
            abs_diff = abs(numbers[i][j] - numbers[ni][nj])
            abs_sum += abs_diff
        abs_sum_all += abs_sum

print(abs_sum_all)