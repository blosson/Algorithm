N, K = map(int, input().split())
burgermen = list(input())                   # 햄버거, 사람 나열을 리스트에 넣어줌

# print(burgermen)

cnt = 0                                     # 최대인원 수 (정답 변수)
for i in range(N):
    if burgermen[i] == 'P':                 # 사람이면
        for j in range(i-K, i+K+1):         # 먹을 수 있는 만큼 거리를 순회
            if 0 <= j < N:                  # 대신 0~N-1 범위여야함
                if burgermen[j] == 'H':     # 햄버거가 있으면
                    burgermen[j] = 0        # 0으로 바꿔줘서 먹었다는 표시 남겨줌
                    cnt += 1                # 먹은 사람 +1
                    break

print(cnt)
