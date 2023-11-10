
def solution(new_id):
    usable = 'abcdefghijklmnopqrstuvwxyz0123456789-_.'  
    # 1
    new_id1 = new_id.lower()

    # 2
    new_id2 = ''
    for s in new_id1:
        if s in usable:
            new_id2 += s

    # 3
    new_id3 = ''
    for i in range(len(new_id2)):
        # 마지막 인덱스 일 때는 범위 벗어나지 않게 조건 설정
        if new_id2[i] == '.' and i < len(new_id2) - 1:
            if new_id2[i+1] == '.':
                continue
        new_id3 += new_id2[i]

    # 4
    new_id4 = new_id3.lstrip('.')
    new_id4 = new_id4.rstrip('.')

    # 5
    if not new_id4:
        new_id5 = 'a'
    else:
        new_id5 = new_id4

    # 6
    if len(new_id5) >= 16:
        new_id6 = new_id5[:15]
        # 이미 앞에서 '.' 중복제거 했으니 그냥 index 하나만 당겨주면 됨 (rstrip도 사용 가능할듯)
        if new_id6[14] == '.':
            new_id6 = new_id6[:14]
    else:
        new_id6 = new_id5

    # 7
    if len(new_id6) <= 2:
        while len(new_id6) < 3:
            new_id6 += new_id6[-1]
    new_id7 = new_id6

    return new_id7


-------
# 2 정규식 풀이

import re

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st



# 3 내 기준 깔끔해보였던 풀이


def solution(new_id):
    answer = ''
    # 1
    new_id = new_id.lower()
    # 2
    for c in new_id:
        if c.isalpha() or c.isdigit() or c in ['-', '_', '.']:
            answer += c
    # 3
    while '..' in answer:
        answer = answer.replace('..', '.')
    # 4
    if answer[0] == '.':
        answer = answer[1:] if len(answer) > 1 else '.'
    if answer[-1] == '.':
        answer = answer[:-1]
    # 5
    if answer == '':
        answer = 'a'
    # 6
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    # 7
    while len(answer) < 3:
        answer += answer[-1]
    return answer