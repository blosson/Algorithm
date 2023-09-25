# prunning 하는 문제 같은데 못 풀겠다..
# 3개 버전 다 4%에서 멈춰서 열불 나서 gg

# ver.1 - append, slicing 사용
N, K = map(int, input().split())
numbers = list(map(int, input().split()))

numbers_sum = []
for i in range(N-K+1):                          # K 길이면 N-K+1개 만큼 합이 생김
    numbers_sum.append(sum(numbers[i:i+K]))     # 슬라이싱한 값들을 리스트에 넣어줌

ans = max(numbers_sum)                          # 최댓값
print(ans)


# ver.2 - 값 넣어주기, slicing 사용
N, K = map(int, input().split())
numbers = list(map(int, input().split()))

numbers_sum = [0] * (N-K+1)
for i in range(N-K+1):
    numbers_sum[i] = sum(numbers[i:i+K])

ans = max(numbers_sum)
print(ans)


# ver.3 - 값 넣어주기, 이중 for문 
N, K = map(int, input().split())
numbers = list(map(int, input().split()))

numbers_sum = [0] * (N-K+1)
for i in range(N-K+1):
    for j in range(K):
        numbers_sum[i] += numbers[i+j]

ans = max(numbers_sum)
print(ans)



