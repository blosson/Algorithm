'''
규칙을 찾아보니 N >= 2일 때
N // 10이 홀수일 때는 앞의 수 다 더한 것에 + 2
N // 10이 짝수일 때는 앞의 수 다 더한 것에 + 1
이 정답의 개수로 나왔다.
'''


def fibo(N):                                # fibo 재귀함수 
    N = int(N / 10)
    if N == 1:                              # 1일 경우는 1
        return 1
    else:
        if N % 2 == 0:                      # 짝수일 경우
            paper_even = 0
            for i in range(1, N):           # 순환하면서 앞의 값들 다 더해줌
                paper_even += fibo(i * 10)  
                ans = paper_even + 2        # + 2
            return ans
        else:
            paper_odd = 0
            for j in range(1, N):           # 순환하면서 앞의 값들 다 더해줌
                paper_odd += fibo(j * 10)
                ans = paper_odd + 1         # + 1
            return ans

for tc in range(1, int(input()) + 1):
    N = int(input())

    print(f'#{tc} {fibo(N)}')

# 시간초과가 뜨면서 10개 중 9개만 정답처리되는데 어떻게 하면 시간을 줄일 수 있을까요..?

            