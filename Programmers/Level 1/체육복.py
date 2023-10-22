# 깊은 복사, 얕은 복사 공부할 것!

def solution(n, lost, reserve):
    # 초기 가져온 인원
    answer = n - len(lost)

    # 계산을 위해 정렬하고 깊은 복사
    lost.sort()
    lost_copy = lost.copy()
    
    # lost와 reserve 둘 다에 있으면 +1 해주고 배열엣 삭제 (복사 안하면 오류남)
    for dude in lost:
        if dude in reserve:
            reserve.remove(dude)
            lost_copy.remove(dude)
            answer += 1
    
    # 이미 정렬했으니 앞번호와 뒷번호 체크해서 최대 인원 수 구하기
    for dude in lost_copy:
        if dude - 1 in reserve:
            reserve.remove(dude-1)
            answer += 1
            continue
            
        elif dude + 1 in reserve:
            reserve.remove(dude+1)
            answer += 1
            continue
      
    return answer