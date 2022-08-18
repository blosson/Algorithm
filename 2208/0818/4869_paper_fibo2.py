'''
규칙을 찾아보니 N >= 2일 때
N // 10이 홀수일 때는 앞의 수 다 더한 것에 + 2
N // 10이 짝수일 때는 앞의 수 다 더한 것에 + 1
이 정답의 개수로 나왔다.
'''


def fibo(N):                            # fibo 재귀함수 
    N = int(N / 10)
    if N == 1:                          # 1일 경우는 1
        return 1
    else:               
        paper = 0
        for i in range(1, N):           # 순환하면서 앞의 값들 다 더해줌
            paper += fibo(i * 10)  
            ans = paper + 2   
        return ans
  

for tc in range(1, int(input()) + 1):

    N = int(input())
    if int(N // 10) % 2 == 0:
        print(f'#{tc} {fibo(N) - 1}')
    else:
        print(f'#{tc} {fibo(N)}')

            