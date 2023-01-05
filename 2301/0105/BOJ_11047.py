# 36ms

N, price = map(int, input().split())
coin_list = list(int(input()) for _ in range(N))    # 코인들 목록 리스트

# print(coin_list)

cnt = 0                                             # 동전이 최소 몇 개 필요한지 (정답 변수)
for coin in coin_list[::-1]:                        # 큰 코인부터 순회 (최소 개수를 구해야하므로)
    # print(coin)
    if price < coin:                                # 현재 가격보다 코인의 가치가 더 크면 필요없으므로 list에서 pop
        coin_list.pop()

    else:                                           # 현재 가격이 코인의 가치보다 더 크면
        how_many = price // coin                    # 몇 개 코인이나 사용할 수 있는지 몫을 구하기 (추가할 갯수)
        cnt += how_many                             # 정답 변수에 갯수를 추가하고
        price -= how_many * coin                    # 가격을 그만큼 빼준다
        coin_list.pop()                             # 그리고 해당 코인은 더 이상 필요 없으므로  pop
    
print(cnt)                                          # 정답 출력