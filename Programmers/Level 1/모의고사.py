# <IDEA>
# 1. 학생 1~3부터 반복되는 찍기 순서를 각 배열에 담는다
# 2. answers의 길이에 맞게 각 사람의 찍기 순서를 순회한다. (answers가 person1~3보다 클 경우 순회할 수 있게 처리하기)
#     - person 1~3 배열의 길이만큼 %를 이용
# 3. 순회하면서 맞는 만큼 cnt를 results 배열에 담아주기
# 4. results의 max를 찾아서 anwer에 담아주고, 만약 동점 시에는 오름차순 정렬
#     - max값을 찾고 results 배열을 순회해서 max값과 일치하면 answer에 append해줌. 그러면 자동으로 오름차순 정렬이 되어있음

def solution(answers):
    person1 = [1, 2, 3, 4, 5]
    person2 = [2, 1, 2, 3, 2, 4, 2, 5]
    person3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    results = [0, 0, 0]
    
    for i in range(len(answers)):
        if answers[i] == person1[i%5]:
            results[0] += 1
        
        if answers[i] == person2[i%8]:
            results[1] += 1
            
        if answers[i] == person3[i%10]:
            results[2] += 1
    # print(results)
    
    max_result = max(results)
    # print(max_result)
    
    answer = []
    for i in range(3):
        if results[i] == max_result:
            answer.append(i+1)

    return answer
