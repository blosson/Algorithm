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