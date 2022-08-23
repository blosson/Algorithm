word = input()

'''
<아이디어>
각 단어를 순회하여 모음이 있는지 확인하고
있다면 삭제한다.
그리고 출력

'''
for i in range(len(word)):
    if word[i] == 'a' or 'e':
        print('wow')