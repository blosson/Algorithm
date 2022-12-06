ans = 0                             # 그룹 단어가 총 몇개인지 (정답변수)
for _ in range(int(input())):
    word = input()
    
    word_len = len(word)            # 단어의 길이
    cnt = 0                         # for문을 돌면서 알파벳이 바뀌는 횟수
    for i in range(word_len - 1):   # 자신의 길이 -1 만큼 반복
        if word[i] != word[i+1]:    # 자신과 다음 문자가 다르면 +1
            cnt += 1

    # print(cnt)                

    if cnt == len(set(word)) - 1:   # word를 (set로 바꾼 뒤 길이 -1)과 cnt가 같으면
        ans += 1                    # 그룹 단어 수 +1

print(ans)
        

    
        