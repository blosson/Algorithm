N = int(input())
vote = list(int(input()) for _ in range(N))

if N == 1:                                              # 후보가 자기자신 1명밖에 없을 경우 cnt = 0
    cnt = 0                                             # 정답 변수 (매수 횟수)

else:                                                   # 후보가 2명 이상일 경우

    cnt = 0                 
    while True:                 
        most_voted = max(vote)                          # 최다득표수
        if most_voted != vote[0]:                       # 최다 득표수가 자기자신(idx 0)이 아니면
            most_voted_index = vote.index(most_voted)   # 해당 인덱스를 찾고
            vote[most_voted_index] -= 1                 # 그 인덱스에 해당하는 값을 -1
            vote[0] += 1                                # 나에게 표를 가져옴 +1
            cnt += 1                                    # 매수 횟수 +1
 
        elif most_voted == vote[0] and vote.count(most_voted) >= 2:     # 최다득표는 맞는데 공동 1위일 경우
            cut_vote = vote[1:]                                         # 자기 자신을 제외한 새로운 list를 만듦 (자기가 idx 0이므로 슬라이싱)
            others_index = cut_vote.index(most_voted) + 1               # 자른 리스트에서 최댓값 인덱스를 찾고 +1을 해줌 (vote 리스트의 원래 인덱스를 찾기 위해)
            vote[others_index] -= 1                                     # 위와 같은 과정 반복
            vote[0] += 1
            cnt += 1
        
        else:                                                           # 단독 1위일 경우 while문 종료
            break


print(cnt)
        


        