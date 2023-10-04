# <IDEA>
# 1. people 배열을 내림차순으로 정렬
# 2. 이미 구명보트에 탑승한 사람들은 탑승대상에서 제외해야하므로 이를 표시해 줄 사람 수만큼의 배열 생성
# 3. people 배열 순회하며 구명보트 인원 계산


#1. 정답 버전
# deque 사용을 위한 import
from collections import deque

def solution(people, limit):
    # 가장 몸무게 많은 사람과 가장 적은 사람끼리 태워야 구명보트를 최소화할 수 있으므로 역순 정렬
    people = sorted(people, reverse = True)
    # pop(0)보다 시간 단출을 위해 people 배열을 deque로 선언
    people = deque(people)
    # print(people)
    
    cnt = 0
    while people:
        # 혼자 남았으면 혼자타면 되므로 pop하고 cnt + 1
        if len(people) == 1:
            people.pop()
            cnt += 1
        
        else:
            # 남아있는 사람 중 가장 무거운 사람과 가벼운 사람의 합이 limit 이하면
            if people[0] + people[-1] <= limit:
                # deque에서 제거 후 cnt +1
                cnt += 1
                people.popleft()
                people.pop()
        
            # 둘을 합쳐 limit 초과면 자기자신만 탑승하므로 cnt+1, deque에서 삭제
            else:
                cnt += 1
                people.popleft()
                        
    return cnt


#2. 시간초과

def solution(people, limit):
    # 가장 몸무게 많은 사람과 가장 적은 사람끼리 태워야 구명보트를 최소화할 수 있으므로 역순 정렬
    people = sorted(people, reverse = True)
    # 이미 보트에 탄 사람들 체크하기 위한 배열
    already = [False] * len(people)
    # print(people, already)
    
    cnt = 0
    # 몸무게 많은 사람부터 순회
    for i in range(len(people)):
        # 이미 탑승 완료했으면 continue
        if already[i] == True:
            continue
            
        # 몸무게 적은 사람부터 확인하기
        for j in range(len(people) - 1, -1, -1):
            # print(i, j)   
            
            # 이미 보트에 탔으면 다음으로 적은 사람으로 확인하러 고고
            if already[j] == True:
                continue
            
            # i == j면 자기 자신이므로 자기만 탑승하고 break
            if i == j:
                cnt += 1
                already[i] = True
                break
                
            else:
                # 둘의 몸무게 합이 구명보트 수용 무게 이하면 보트수 + 1, 탑승처리(True)
                if people[i] + people[j] <= limit:
                    # print(people[i], people[j])
                    cnt += 1
                    already[i], already[j] = True, True
                    break
                    
    return cnt


# 미친 풀이
def solution(people, limit) :
    answer = 0
    people.sort()

    a = 0
    b = len(people) - 1
    while a < b :
        if people[b] + people[a] <= limit :
            a += 1
            answer += 1
        b -= 1
    return len(people) - answer