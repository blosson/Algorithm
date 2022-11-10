N = int(input())
for i in range(N):
    ox = input()
    score = 0
    cnt = 0
    for i in range(len(ox)):
        if ox[i] == 'X':
            cnt = 0
        else:       # 'O'인 경우
            cnt += 1
        score += cnt

    print(score)

    

            