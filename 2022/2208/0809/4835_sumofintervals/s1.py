# sum 함수 정의
def sssssum(arg):
    result = 0
    for i in arg:
        result += i
    return result
        

test_case = int(input())

n = 1
while n <= test_case:

    N, M = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
		
		# 최대 이웃합
    sum_king = sssssum(numbers[0:M]) # 첫번째 이웃합
    for i in range(N-M+1): # 총 (N+M-1)개의 이웃합을 만들 수 있음
        if sum_king < sssssum(numbers[i:i+M]):
            sum_king = sssssum(numbers[i:i+M])
		
		# 최소 이웃합
    sum_slave = sssssum(numbers[0:M])
    for i in range(N-M+1): 
        if sum_slave > sssssum(numbers[i:i+M]):
            sum_slave = sssssum(numbers[i:i+M])

    ans = sum_king - sum_slave
    print(f'#{n} {ans}')

    n = n + 1







