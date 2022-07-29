

T = int(input())


for i in range(T):
    N = int(input())
    game_money = N * 100
    max_game = int(game_money / 2)

    print(f'#{i+1} {max_game}')