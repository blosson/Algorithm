# <IDEA>
# 1. progress와 speed 배열을 순회해서 배포까지 며칠 씩 작업이 필요한지 계산하여 새로운 배열에 넣음
# 2. while문 안에서 순회를 해서 (조건 모든 배열이 0일 때 종료)
# 3. 숫자가 더 작은 것들을 모두 cnt + 1씩 해서 answer 배열에 담아줌, 완료한 것들은 0으로 변경
#     - 그 앞에 아직 완료되지 않은 것들이 있으면 바꾸지 말기


def solution(progresses, speeds):
    answer = []
    # 작업 완료시까지 걸릴 날의 수를 담을 배열 을 생성하고 for으로 계산해서 넣어줌
    days = [0] * len(progresses)
    for i in range(len(progresses)):
        progress = progresses[i]
        cnt = 0
        while progress < 100:
            progress += speeds[i]
            cnt += 1
        days[i] = cnt
    # print(days)
    
    for i in range(len(days)):
        # 이미 배포가 되었으면 다음 progress 확인하러 가기
        if days[i] == 0:
            continue
        
        # 자기자신도 배포에 포함되므로 cnt는 1로 시작
        cnt = 1
        # 자기 다음 차례부터 끝까지 순회하면서 함께 배포될 progress가 있는지 확인
        for j in range(i+1, len(days)):
            # 아직 배포가 되지 않았거나 i보다 작업날이 빠른 경우
            if days[j] != 0 and days[j] <= days[i]:
                # AND, 앞의 progress들이 모두 배포가 된 경우
                if sum(days[i+1:j]) == 0:  
                    days[j] = 0
                    cnt += 1
                    
        answer.append(cnt)
                
    return answer