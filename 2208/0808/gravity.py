'''
2차원으로 보이는 것을 1차원 리스트로 바꾸어 풀면 할만한 문제.
자신의 오른쪽 값들의 값을 비교해서 공백인 칸을 어떻게 구할 것이냐가 핵심이었다.

'''

N = int(input())
boxes = list(map(int, input().split()))

max_cnt = 0             
for i in range(N):              
    cnt = 0
    for j in range(i+1, N):         # 자신의 바로 오른쪽부터 끝까지
        if boxes[i] > boxes[j]:     # 자기가 더 크면 +1
            cnt += 1
    if max_cnt < cnt:
        max_cnt = cnt

print(max_cnt)