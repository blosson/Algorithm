'''
1. 기본적으로 첫 주사위의 윗부분을 어떤 수로 할지 경우의 수를 6가지로 가정
2. A~F 각 인덱스는 (0, 5), (1, 3), (2, 4)를 마주봄 -> 이후 최댓값을 구할 때 쓰임
3. 현재 주사위의 윗부분과 다음 주사위의 아랫부분을 어떻게 연결시키고 그에 따른 최댓값을 어떻게 구할지가 핵심인 것 같다.
'''


N = int(input())
dices = [list(map(int, input().split())) for _ in range(N)]     # 주사위 숫자 입력 

sum_max = 0                                                     # 주사위 최댓값 (정답)
for i in range(1, 7):                                           # 주사위 눈 갯수가 1~6이므로 이렇게 범위 설정
    sum_num = 0                                                 # 1~6까지 경우의 수 안에서의 주사위 숫자의 합
    for j in range(1, N):
        if j == 1:

            # 첫 번째 주사위
            first_dice_index_up = dices[0].index(i)             # 첫 번째 주사위의 윗부분 숫자 인덱스

            if first_dice_index_up == 0:                        # 윗부분이 0일때 아랫부분의 인덱스는 5 (아래도 이와 같이 진행)
                first_dice_index_down = 5
                if (dices[0][first_dice_index_up] == 5 and dices[0][first_dice_index_down] == 6) or (dices[0][first_dice_index_up] == 6 and dices[0][first_dice_index_down] == 5):
                    sum_num += 4                                # 윗부분과 아랫부분이 5와 6이면 옆면의 최댓값이 4이므로 추가
                elif dices[0][first_dice_index_up] == 6 or dices[0][first_dice_index_down] == 6:
                    sum_num += 5                                # 둘 중 하나만 6이면 옆면의 최댓값이 5이므로 추가
                else:                                           
                    sum_num += 6                                # 위아래에 6이 없으면 옆면의 최댓값이 무조건 6이므로 추가

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
            index_down = dices[1].index(i)                     # 두 번째 주사위 윗면 인덱스

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
            
        # 3번째 주사위부터 (j가 2 이상일 때)
        else:
            index_down = dices[j].index(dices[j-1][index_up])           # 3 번째 주사위 윗면 인덱스
            
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

    if sum_num > sum_max:                              # 1~6까지 가장 큰 합을 sum_max에 저장
        sum_max = sum_num

print(sum_max)
        
    
    