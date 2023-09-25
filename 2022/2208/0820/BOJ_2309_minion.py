m1 = int(input())    # 난쟁이들 키 입력
m2 = int(input())
m3 = int(input())
m4 = int(input())
m5 = int(input())
m6 = int(input())
m7 = int(input())
m8 = int(input())
m9 = int(input())

height_list = [m1, m2, m3, m4, m5, m6, m7, m8, m9]   # 난쟁이 키 리스트로 입력
height_sum = sum(height_list)                        # 키 전부 더해주기
height_diff = height_sum - 100                       # 키의 합 - 100 (우리가 구할 목표값)

blank_list = []                                      # 9C2 중 합이 height_diff가 되는 두 원소를 찾아 넣어줄 빈 리스트
for i in range(9):                                   # for문 돌리자
    for j in range(9):
        if i != j:                                   # 자기 자신이 아니면
            if height_list[i] + height_list[j] == height_diff:    # 두 원소값이 height_diff와 같으면
                blank_list.append(height_list[i])                 # blank 리스트에 넣어줌
                blank_list.append(height_list[j])
                break                               # 시간 절약을 위해 break 두개 걸어줌
                break                               # (근데 왜 추가 리스트에 추가 원소들이 생기지.. [15, 25, 25, 15] 이렇게

del1 = blank_list[0]                                # 삭제할 값들 변수에 저장
del2 = blank_list[1]

height_list.remove(del1)                            # height_list에서 가짜 난쟁이 키들 삭제
height_list.remove(del2)

height_list.sort()                                  # 정렬
for i in height_list:                               # for문 돌려서 형식에 맞게 정답 출력
    print(i)



                
