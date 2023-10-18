# <IDEA>
# - k값이 항상 사과 안에 있다고 가정 (그렇지 않으면 문제가 좀 이상함)
# 1. 총 몇개의 상자가 나오는지 len으로 계산하고, score를 오름차순 정렬하여 앞에서부터 m개씩 상자에 담음 (or scores 길이가 길어질 수 있으니 딕셔너리 형태가 좋을 것 같음)
# 2. 각 상자 배열(or 딕셔너리 value)에서 최솟값을 구하고 * m을 해서 answer에 +해줌


def solution(k, m, score):
    answer = 0
    boxes = {}                              # 박스별 사과 score 담을 딕셔너리
    box_num = len(score) // m               # 총 박스 개수
    # print(box_num)
    score.sort(reverse=True)                # 최댓값을 구해야하기 때문에 편의상 내림차순 정렬
    
    for i in range(box_num):                # 각 상자별로 점수가 높은 순서대로 사과 넣어주기
        boxes[i] = score[(i*m):(i*m)+m]
    
    for value in boxes.values():            # 상자별 순회해서 최소 점수 * 갯수를 answer에 더해주기
        answer += min(value) * m
    # print(answer)
    
    return answer



-------
# 파이써닉한 풀이
def solution(k, m, score):
    answer = 0
    score.sort(reverse=True) #점수 내림차순 정렬
    answer = sum([score[i+m-1] for i in range(0,len(score),m) if i+m <= len(score)])*m  
    return answer