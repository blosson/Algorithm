
T = int(input())

for i in range(T):
    N = int(input()) # 솔직히 이건 의미가 없지 않나? N을 근거로 N_ppl에서 리스트를 받아올 때 제약을 줄 수는 없을까?
    N_ppl = list(map(int, input().split())) # map 함수  다시 공부하자..
    # print(N_ppl) 왜 이건 그냥 주소가 뜨고
    # print(list(N_ppl)) 이건 이건 리스트 형태로 뜰까

    count = 0
    while True:
        N_ppl.sort(reverse=True) # 정렬해서 가장 큰 2개 보여주기
        if N_ppl[1] != 0: # 2번째로 큰 숫자가 0이면(게임을 못하게 됨)
            N_ppl[0] -= 1
            N_ppl[1] -= 1
            count += 1
        else:
            break
    print(f'#{i+1} {count}')

    