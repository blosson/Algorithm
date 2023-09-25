# BOJ 14696 딱지놀이

for i in range(int(input())):
    A, *a = list(map(int, input().split()))
    B, *b = list(map(int, input().split()))
    # 좀 더 스마트하게 입력값을 받을 수 있는 방법은 없을까? 가변인자!

    a_list = [0] * 4
    b_list = [0] * 4

    for x in a:
        if x == 4:
            a_list[0] += 1
        elif x == 3:
            a_list[1] += 1
        elif x == 2:
            a_list[2] += 1
        elif x == 1:
            a_list[3] += 1
    print(a_list)

    for y in b:
        if y == 4:
            b_list[0] += 1
        elif y == 3:
            b_list[1] += 1
        elif y == 2:
            b_list[2] += 1
        elif y == 1:
            b_list[3] += 1
    print(b_list)

    for k in range(4):
        if a_list[k] > b_list[k]:
            print('A')
            break
        elif a_list[k] < b_list[k]:
            print('B')
            break
    # 여기서 무승부일 때 어떻게 해야할지 모르겠습니다..
        

    
    