# <IDEA>
# - 탈락하는 경우 : 끝말과 시작하는 알파벳이 다를 때, 이미 나온 단어를 말했을 때
#     1. 배열을 순회하며 이전 단어 끝 글자와 확인, used에 존재하는 지 확인 (첫 단어는 예외처리)
#         - 문제시 break 하고 정답출력
#     2. 단어를 used 배열에 추가
#     3. idx 끝에 다다랐는데도 문제 없으면 [0, 0] 정답 출력
# - 사람 번호 구하기, 몇 번째 차례인지
#     - words의 idx를 3으로 나눈 나머지 + 1이 그 사람의 번호
#     - idx를 3으로 나눈 몫 + 1


#1 내 풀이
def solution(n, words):
    answer = []
    used = []
    for i in range(len(words) + 1):
        # 마지막 단어까지 말한 후 이상 없을 시 [0, 0] 출력
        if i == len(words):
            answer = [0, 0]
            break
        
        # 첫 번째 단어일 때 예외처리 (그냥 추가)
        if i == 0:
            used.append(words[i])
        
        # 두 번째 ~ 마지막 단어
        else:
            # 이미 말한 단어면, 사람 번호와 순서 answer에 입력
            if words[i] in used:
                person = (i % n) + 1
                turn = (i // n) + 1
                answer = [person, turn]
                break
            
            # 말하지 않은 단어면 앞 단어의 끝글자와 현재 단어의 첫 글자 비교
            else:
                if words[i-1][-1] == words[i][0]:
                    used.append(words[i])
                # 글자가 다르면 번호, 순서 answer에 담음
                else:
                    person = (i % n) + 1
                    turn = (i // n) + 1
                    answer = [person, turn]
                    break
        
    return answer

----------
#2 깔끔한 풀이

def solution(n, words):
    for p in range(1, len(words)):
        if words[p][0] != words[p-1][-1] or words[p] in words[:p]: return [(p%n)+1, (p//n)+1]
    else:
        return [0,0]