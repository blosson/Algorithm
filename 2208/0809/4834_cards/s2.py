
test_case = int(input())

for tc in test_case:
    N = int(input())
    cards = list(map(int, input()))

    cnt_list = [0] * 10
    
    for i in cards:
        cnt_list[i] += 1

    cnt_max = 0
    max_idx = 0
    for j in range(len(cnt_list)):
        if cnt_list[j] >= cnt_max:
            cnt_max = cnt_list[j]
            max_idx = j

    print(f'#{tc+1} {mac_idx} {cnt_max}')

        



