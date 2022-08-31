for tc in range(1, int(input()) + 1):

    N = int(input())
    cards = input()

    card_count = [0] * 10
    for card in cards:
        card_count[int(card)] += 1

    cnt_max = 0
    max_idx = -1
    for i in range(len(card_count)):
        if card_count[i] >= cnt_max:
            max_idx = i
            cnt_max = card_count[i]

    print(f'#{tc} {max_idx} {cnt_max}')
        
    
    
    