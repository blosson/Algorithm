
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