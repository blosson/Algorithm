N = int(input())
dices = [list(map(int, input().split())) for _ in range(N)]

sum_max = 0
for i in range(1, 7):
    sum_num = 0
    for j in range(1, N):
        if j == 1:
            # 첫 번째 주사위

            first_dice_index_up = dices[0].index(i)

            if first_dice_index_up == 0:
                first_dice_index_down = 5
                if (dices[0][first_dice_index_up] == 5 and dices[0][first_dice_index_down] == 6) or (dices[0][first_dice_index_up] == 6 and dices[0][first_dice_index_down] == 5):
                    sum_num += 4
                elif dices[0][first_dice_index_up] == 6 or dices[0][first_dice_index_down] == 6:
                    sum_num += 5
                else:
                    sum_num += 6

            elif first_dice_index_up == 1:
                first_dice_index_down = 3
                if (dices[0][first_dice_index_up] == 5 and dices[0][first_dice_index_down] == 6) or (dices[0][first_dice_index_up] == 6 and dices[0][first_dice_index_down] == 5):
                    sum_num += 4
                elif dices[0][first_dice_index_up] == 6 or dices[0][first_dice_index_down] == 6:
                    sum_num += 5
                else:
                    sum_num += 6

            elif first_dice_index_up == 2:
                first_dice_index_down = 4
                if (dices[0][first_dice_index_up] == 5 and dices[0][first_dice_index_down] == 6) or (dices[0][first_dice_index_up] == 6 and dices[0][first_dice_index_down] == 5):
                    sum_num += 4
                elif dices[0][first_dice_index_up] == 6 or dices[0][first_dice_index_down] == 6:
                    sum_num += 5
                else:
                    sum_num += 6

            elif first_dice_index_up == 3:
                first_dice_index_down = 1
                if (dices[0][first_dice_index_up] == 5 and dices[0][first_dice_index_down] == 6) or (dices[0][first_dice_index_up] == 6 and dices[0][first_dice_index_down] == 5):
                    sum_num += 4
                elif dices[0][first_dice_index_up] == 6 or dices[0][first_dice_index_down] == 6:
                    sum_num += 5
                else:
                    sum_num += 6

            elif first_dice_index_up == 4:
                first_dice_index_down = 2
                if (dices[0][first_dice_index_up] == 5 and dices[0][first_dice_index_down] == 6) or (dices[0][first_dice_index_up] == 6 and dices[0][first_dice_index_down] == 5):
                    sum_num += 4
                elif dices[0][first_dice_index_up] == 6 or dices[0][first_dice_index_down] == 6:
                    sum_num += 5
                else:
                    sum_num += 6

            elif first_dice_index_up == 5:
                first_dice_index_down = 0
                if (dices[0][first_dice_index_up] == 5 and dices[0][first_dice_index_down] == 6) or (dices[0][first_dice_index_up] == 6 and dices[0][first_dice_index_down] == 5):
                    sum_num += 4
                elif dices[0][first_dice_index_up] == 6 or dices[0][first_dice_index_down] == 6:
                    sum_num += 5
                else:
                    sum_num += 6
            

            # 두 번째 주사위
            index_down = dices[j].index(i)

            if index_down == 0:
                index_up = 5
                if (dices[j][index_down] == 5 and dices[j][index_up] == 6) or (dices[j][index_down] == 6 and dices[j][index_up] == 5):
                    sum_num += 4
                elif dices[j][index_down] == 6 or dices[j][index_up] == 6:
                    sum_num += 5
                else:
                    sum_num += 6

            elif index_down == 1:
                index_up = 3
                if (dices[j][index_down] == 5 and dices[j][index_up] == 6) or (dices[j][index_down] == 6 and dices[j][index_up] == 5):
                    sum_num += 4
                elif dices[j][index_down] == 6 or dices[j][index_up] == 6:
                    sum_num += 5
                else:
                    sum_num += 6

            elif index_down == 2:
                index_up = 4
                if (dices[j][index_down] == 5 and dices[j][index_up] == 6) or (dices[j][index_down] == 6 and dices[j][index_up] == 5):
                    sum_num += 4
                elif dices[j][index_down] == 6 or dices[j][index_up] == 6:
                    sum_num += 5
                else:
                    sum_num += 6

            elif index_down == 3:
                index_up = 1
                if (dices[j][index_down] == 5 and dices[j][index_up] == 6) or (dices[j][index_down] == 6 and dices[j][index_up] == 5):
                    sum_num += 4
                elif dices[j][index_down] == 6 or dices[j][index_up] == 6:
                    sum_num += 5
                else:
                    sum_num += 6

            elif index_down == 4:
                index_up = 2
                if (dices[j][index_down] == 5 and dices[j][index_up] == 6) or (dices[j][index_down] == 6 and dices[j][index_up] == 5):
                    sum_num += 4
                elif dices[j][index_down] == 6 or dices[j][index_up] == 6:
                    sum_num += 5
                else:
                    sum_num += 6

            elif index_down == 5:
                index_up = 0
                if (dices[j][index_down] == 5 and dices[j][index_up] == 6) or (dices[j][index_down] == 6 and dices[j][index_up] == 5):
                    sum_num += 4
                elif dices[j][index_down] == 6 or dices[j][index_up] == 6:
                    sum_num += 5
                else:
                    sum_num += 6
            

        else:
            index_down = index_up
            
            if index_down == 0:
                index_up = 5
                if (dices[j][index_down] == 5 and dices[j][index_up] == 6) or (dices[j][index_down] == 6 and dices[j][index_up] == 5):
                    sum_num += 4
                elif dices[j][index_down] == 6 or dices[j][index_up] == 6:
                    sum_num += 5
                else:
                    sum_num += 6

            elif index_down == 1:
                index_up = 3
                if (dices[j][index_down] == 5 and dices[j][index_up] == 6) or (dices[j][index_down] == 6 and dices[j][index_up] == 5):
                    sum_num += 4
                elif dices[j][index_down] == 6 or dices[j][index_up] == 6:
                    sum_num += 5
                else:
                    sum_num += 6

            elif index_down == 2:
                index_up = 4
                if (dices[j][index_down] == 5 and dices[j][index_up] == 6) or (dices[j][index_down] == 6 and dices[j][index_up] == 5):
                    sum_num += 4
                elif dices[j][index_down] == 6 or dices[j][index_up] == 6:
                    sum_num += 5
                else:
                    sum_num += 6

            elif index_down == 3:
                index_up = 1
                if (dices[j][index_down] == 5 and dices[j][index_up] == 6) or (dices[j][index_down] == 6 and dices[j][index_up] == 5):
                    sum_num += 4
                elif dices[j][index_down] == 6 or dices[j][index_up] == 6:
                    sum_num += 5
                else:
                    sum_num += 6

            elif index_down == 4:
                index_up = 2
                if (dices[j][index_down] == 5 and dices[j][index_up] == 6) or (dices[j][index_down] == 6 and dices[j][index_up] == 5):
                    sum_num += 4
                elif dices[j][index_down] == 6 or dices[j][index_up] == 6:
                    sum_num += 5
                else:
                    sum_num += 6

            elif index_down == 5:
                index_up = 0
                if (dices[j][index_down] == 5 and dices[j][index_up] == 6) or (dices[j][index_down] == 6 and dices[j][index_up] == 5):
                    sum_num += 4
                elif dices[j][index_down] == 6 or dices[j][index_up] == 6:
                    sum_num += 5
                else:
                    sum_num += 6
    print(sum_num)
    print(sum_max)

#     if sum_num > sum_max:
#         sum_max = sum_num

# print(sum_max)
        
    
    