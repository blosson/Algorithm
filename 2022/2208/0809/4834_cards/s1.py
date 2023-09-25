test_case = int(input())

n = 1
while n <= test_case:
    how_many_cards = int(input()) # 카드 장수
    cards = input() # 카드숫자 (str! 0이 제일 앞에 올 수 있으므로)

    king = cards[0] # 가장 많은 카드 (초기값은 index 0으로 시작)
    for i in range(len(cards)):
        if cards.count(cards[i]) > cards.count(king): # index i 값과 king 값 중에 어떤 것이 더 많은 지 비교 (i 값이 더 많으면)
            king = cards[i] # 새롭게 king 할당
        elif cards.count(cards[i]) == cards.count(king): # count가 같으면
            if int(king) >= int(cards[i]): # str -> int 로 형 변환에서 숫자 크기 비교
                pass
            else: # i 값이 더 큰 숫자면 
                king = cards[i] # king에 cards[i]에 해당하는 값 할당

    print(f'#{n} {king} {cards.count(king)}')

    n += 1

# count 함수를 어떻게 만들 수 있을까? 아니면 최소한 리스트 요소들의 빈도수를 셀 수 있는 방법이라도..async


            