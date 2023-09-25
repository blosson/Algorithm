standard = 'abcdefghijklmnopqrstuvwxyz'     # 알파벳 순서

for tc in range(1, int(input()) + 1):
    word = input()
    max_cnt = 0

    for i in range(len(word)):
        cnt = 0
        if word[:i+1] in standard[:i+1]:    # 슬라이싱해서 앞부분이 일치하는 길이만큼 cnt에 숫자 넣어줌
            cnt = i + 1
            
            if max_cnt < cnt:
                max_cnt = cnt

    print(f'#{tc} {max_cnt}')