def f(i, k):
    global ans 
    
    if i == k:
        run = 0
        tri = 0
        if card[0] == card[1] and card[1] == card[2]:
            tri += 1
        print(card)
    else:
        for j in range(i, k):
            pass
            

for tc in range(1, int(input()) + 1):
    card = list(map(int, input()))
    ans = 'Lose'
    
    