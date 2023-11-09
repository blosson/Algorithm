# <IDEA>
# 1. survey를 순회해서 각 성격 유형 별 점수를 기록한다.
#     - survey[i]의 0번 인덱스에 따라서 질문이 달라지므로 index[0]에 따른 점수 부여 조건을 다르게 주어야 함
#     - RT / CF / JM / AN 미리 나눠서 만들어두기 → 리스트의 안의 딕셔너리 형태로 만들어서 나중에 lambda 정렬하기 편하게!
# 2. 사전순 - 오름차순 정렬 (lambda 함수 사용하자)

# lambda 함수 정렬, for문 안의 이중 list or dict 값 변경

def solution(survey, choices):
    answer = ''
    scores = [{'R':0, 'T':0}, {'C':0, 'F':0}, {'J':0, 'M':0}, {'A':0, 'N':0}]
    
    for i in range(len(survey)):
        if choices[i] <= 3:
            for idx, score in enumerate(scores):
                if survey[i][0] in score.keys():
                    scores[idx][survey[i][0]] += 4 - choices[i]
                    
        elif choices[i] >= 5:
            for idx, score in enumerate(scores):
                if survey[i][1] in score.keys():
                    scores[idx][survey[i][1]] += choices[i] - 4    
                    
    for score in scores:
        # key 값만 list 형태로 정렬해서 뽑아오는 법
        score = sorted(score, key=lambda x : score[x], reverse=True)
        # score = sorted(score, key=score.get, reverse=True)
        answer += score[0]
        
        # key, value 모두 보이게 정렬
        # score = sorted(score.items(), key=lambda x : -x[1])   
        # answer += score[0][0]

    return answer




----
# 걍 질문
for score in scores:
        if 'R' in score.keys():
            score['R'] = 1000
    print(scores)

------
[{'R': 1000, 'T': 3}, {'C': 0, 'F': 0}, {'J': 0, 'M': 0}, {'A': 0, 'N': 0}]
------
여기서 왜 scores가 변경되는 걸까?