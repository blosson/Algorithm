def solution(dartResult):
    cnt = 0             # 라운드 cnt           
    score = [0, 0, 0]   # 각 기회별 점수판
    for s in range(len(dartResult)):
        
        # 숫자의 경우 (10인 경우도 예외처리 해주어야함)
        if dartResult[s].isdigit():
            if dartResult[s] == '1' and dartResult[s+1] == '0':
                score[cnt] = 10
            elif dartResult[s] == '0':
                pass
            else:
                score[cnt] = int(dartResult[s])
         
        # single, double, triple 경우 (각 라운드에 한 번씩 나오므로 뒤에 cnt+1)
        if dartResult[s] == 'S':
            cnt += 1
        if dartResult[s] == 'D':
            score[cnt] **= 2
            cnt += 1
        if dartResult[s] == 'T':
            score[cnt] **= 3
            cnt += 1
        
        # *의 경우 3가지 조건으로 나누어줌 (문자 뒤에 *, #가 오므로 cnt는 1~3)
        if dartResult[s] == '*':
            if cnt == 1:
                score[0] *= 2
            if cnt == 2:
                score[0] *= 2
                score[1] *= 2
            if cnt == 3:
                score[1] *= 2
                score[2] *= 2 
            
        
        if dartResult[s] == '#':
            score[cnt-1] *= -1
    
    answer = sum(score)
        
        
    return answer