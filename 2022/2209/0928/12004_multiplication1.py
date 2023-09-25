def multiplication(N):
    global ans

    for a in range(1, 10):          # 1~9 이중 for문 순회해서 a*b 값이 N이 나오면
        for b in range(1, 10):
            if a * b == N:
                ans = 'Yes'         # ans를 Yes로 바꾸고 함수 종료
                return ans
    

for tc in range(1, int(input()) + 1):
    N = int(input())
    ans = 'No'                      # 기본적으로 no 
    multiplication(N)
    
    print(f'#{tc} {ans}')