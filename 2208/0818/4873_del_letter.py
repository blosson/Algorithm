for tc in range(1, int(input()) + 1):

    word = input()
    word_list = list(word)                          # str 형태는 삭제가 안돼서 list로 변환

    while True:
        for i in range(len(word_list)):
            if i == len(word_list) - 1:             # 마지막 글자면 멈춰!
                break
            else:
                if word_list[i] == word_list[i+1]:  # list의 i값과 i+1이 같은지 확인
                    del word_list[i:i+2]            # 같으면 2글자 삭제 후 멈춰! 
                    break                           # Q : break 안 쓰고 문제를 풀 수 있을까?

        cnt = 0                         
        for j in range(len(word_list)):             # 연속되는 같은 두 글자가 있는지 확인하는 for문
            if j == len(word_list) - 1:             # 마지막 글자면 멈춰!
                break
            if word_list[j] == word_list[j+1]:
                cnt += 1                            
        if cnt == 0:                                # 존재하지 않으면 결과 출력
            break
                                                    # 존재하면 while문 반복
    print(f'#{tc} {len(word_list)}')
