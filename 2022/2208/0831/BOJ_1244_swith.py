N = int(input())
swith = [2] + list(map(int, input().split()))       # 인덱싱 편의를 위해 인덱스 0에 2를 넣어줌
num_student = int(input())
for i in range(num_student):
    gen_num = list(map(int, input().split()))

    if gen_num[0] == 1:                             # 남학생
        how_many = (len(swith) - 1) // gen_num[1]   # 곱셈 구간 정하기 위한 변수 (처음에 index 0 넣어줘서 -1을 뺌) 
        for i in range(1, how_many + 1):            
            object = i * gen_num[1]                 # 스위치 상태 바꿀 인덱스
            if swith[object] == 0:                  # 0 -> 1
                swith[object] = 1
            else:                                   # 1 -> 0
                swith[object] = 0

    else:                                           # 여학생
        surroundnig_num = 1
        #left_index = gen_num[1] - surroundnig_num   왜 이렇게 하면 자동으로 surrounding_num의 변화에 따라 바뀌지 않을까    
        #right_index = gen_num[1] + surroundnig_num
        while True:
            left_index = gen_num[1] - surroundnig_num                  # 구간
            right_index = gen_num[1] + surroundnig_num
            if left_index == 0 or (right_index == len(swith) + 1):     # 양 끝값이 마지막이면
                if swith[gen_num[1]] == 0:                             # 자기 자신 인덱스만 바꾸고 종료
                    swith[gen_num[1]] = 1
                else:
                    swith[gen_num[1]] = 0
                break        

            else:                                                     # 좌우 범위 만큼 똑같으면
                if swith[left_index] == swith[right_index]:           
                    if swith[left_index] == 0:                        # 아 그냥 이거 함수로 만들걸..
                        swith[left_index] = 1
                        swith[right_index] = 1
                    else:
                        swith[left_index] = 0
                        swith[right_index] = 0
                    surroundnig_num += 1

                else:
                    if swith[gen_num[1]] == 0:
                        swith[gen_num[1]] = 1
                    else:
                        swith[gen_num[1]] = 0
                    break              


swith.pop(0) # index[0] 제거
for i in range((len(swith) // 20) + 1):
    print_index = (20 * i)
    print(*swith[:20])
    swith = swith[20:]
    if swith == []:
        break

