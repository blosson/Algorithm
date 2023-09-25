def babygin(arr):
    for i in range(10):
        if arr[i] >= 3:                                                   # triple 검사 
            return True
        if i <= 7 and arr[i] >= 1 and arr[i+1] >= 1 and arr[i+2] >= 1:    # run 검사 (8, 9는 +2 만큼의 인덱스가 없으므로 생략)
            return True

for tc in range(1, int(input()) + 1):
    cards = list(map(int, input().split()))
    player1 = [0] * 10                          # 각 숫자에 해당하는 인덱스에 카드 개수를 저장할 리스트
    player2 = [0] * 10
    ans = 0                                     # 기본 세팅 = 무승부


    for i in range(6):
        player1[cards[2*i]] += 1                # index 0, 2, 4... 카드를 player1에게 나누어 줌
        player2[cards[2*i + 1]] += 1            # index 1, 3, 5... 카드를 player2에게 나누어 줌
        if i >= 2:                              # 플레이어들에게 카드가 3장 이상 모이면 babygin 확인
            if babygin(player1):
                ans = 1
                break
            if babygin(player2):
                ans = 2
                break
    print(f'#{tc} {ans}')
    
    

# 내 풀이.. 뭔가 잘 안돼서 다시 해보려고 합니다.

# def babygin(arr):
#     sorted_arr = sorted(arr)
    
#     for i in range(len(arr)):
#         if sorted_arr.count(sorted_arr[i]) >= 3:
#             pass


# cards = list(map(int, input().split()))     # []로 감싸면 그냥 map 타입으로 출력되는구나..
# player1 = []
# player2 = []

# for i in range(12):
#     if i % 2 == 0:
#         player1.append(cards[i])
#         if i >= 4:
#             pass
#     else:
#         player2.append(cards[i])
#         if i >= 5:
#             pass

# print(player1)
# print(player2)
    