N, K = map(int, input().split())

room_cnt = 0
students_list = [[], [], [], [], [], []]
for _ in range(N):
    S, Y = map(int, input().split())
    student_info = [0, 0]
    student_info[0] = S
    student_info[1] = Y
    for i in range(1, 6):
        if student_info[1] == i:
            students_list[i-1].append(student_info)

for i in range(1, 7):
    if students_list[i]



    

    