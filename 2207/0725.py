T = int(input())

# 입력을 먼저 받게 해야지
list = []
for k in range(1, T+1):
    list.append(k)


while True:
    N = int(input())
    if 1 <= N <= 10:
        break
    else: 
        print('1 이상 10 이하의 정수를 입력하세요.')
sum = 0
for i in range(1, N+1):
    if i % 2 == 1:
        sum = sum + i
    else:
        sum = sum - i
print(f'#{k} {sum}', end = '')

# why not
# why!!!!