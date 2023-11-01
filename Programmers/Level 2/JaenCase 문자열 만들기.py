# <IDEA>
# join 함수, string의 upper, lower, capitalize 특성 이용

def solution(s):
    s = s.split(" ")
    for i in range(len(s)):
        s[i] = s[i][:1].upper() + s[i][1:].lower()
    return ' '.join(s)


def solution(s):
    answer = ''
    s=s.split(' ')
    for i in range(len(s)):
        # capitalize 내장함수를 사용하면 첫 문자가 알파벳일 경우 대문자로 만들고
        # 두번째 문자부터는 자동으로 소문자로 만든다
        # 첫 문자가 알파벳이 아니면 그대로 리턴한다
        s[i]=s[i].capitalize()
    answer=' '.join(s)
    return answer


def solution(s):
    answer = ''
    s_list = s.split(' ')
    for word in s_list:
        # word = word.strip(' ')
        if not word[0].isdigit():
            new_word = word[0].upper() + word[1:].lower()
            answer += ' ' + new_word
        else:
            if word[0] == ' ':
                answer += word
            else:
                new_word = word[0] + word[1:].lower()
                answer += ' ' + new_word     
    
    answer = answer.lstrip(' ')
    return answer