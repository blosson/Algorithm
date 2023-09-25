N, K = map(int, input().split())                        # 학생 수, 방의 정원 입력

students_list = [[], [], [], [], [], []]                # 1~6학년의 정보를 담을 빈 리스트 생성
for _ in range(N):                                      # 각 학생의 정보 for문 안에서 입력받아 students_list에 넣어주기
    S, Y = map(int, input().split())
    student_info = [0, 0]                               # 성별과 학년을 담을 빈 리스트
    student_info[0] = S                                 # 학생별 성별 리스트에 삽입
    student_info[1] = Y                                 # 학생별 학년 리스트에 삽입
    for i in range(1, 7):
        if student_info[1] == i:                        # 각 학생별 학년 정보를 바탕으로 students_list의 학년별 index에 넣어줌
            students_list[i-1].append(student_info)

# print(student_list) ---> 각 학년별 정보가 담긴 리스트를 볼 수 있음

room_cnt = 0                                            # 방이 몇개나 필요한지 세는 변수
for i in range(6): 
    girl_cnt = 0
    boy_cnt = 0
    for j in range(len(students_list[i])):              # 여학생, 남학생 성별 확인 후 각각 몇명이나 있는지 cnt에 넣어주기
        if students_list[i][j][0] == 0:                 # 여학생
            girl_cnt += 1
        else:                                           # 남학생
            boy_cnt += 1

    if girl_cnt == 0:                                   # 성별에 한 명도 없으면 방이 필요 없으므로 pass
            pass
    elif girl_cnt % K == 0:                             # 방의 정원과 딱 나누어 떨어지면 몫 만큼만 필요하니 room_cnt에 추가
        room_cnt += (girl_cnt // K)
    else:
        room_cnt += (girl_cnt // K + 1)                 # 한 명 이상이고 정원과 나누어 떨어지지 않으면 (몫 + 1)만큼 room_cnt에 추가

    if boy_cnt == 0:                                    # 남학생도 같은 과정 반복
        pass
    elif boy_cnt % K == 0:
        room_cnt += (boy_cnt // K)
    else:
        room_cnt += (boy_cnt // K + 1)


print(room_cnt)                                         # 정답 출력

        
 


    

    