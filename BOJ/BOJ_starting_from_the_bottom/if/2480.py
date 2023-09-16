dice = list(map(int, input().split()))

for i in dice:
    if dice.count(i) == 3:
        ans = 10000 + (i * 1000)
        break
    elif dice.count(i) == 2:
        ans = 1000 + (i * 100)
        break
    else:
        dice_max = max(dice)
        ans = dice_max * 100

print(ans)