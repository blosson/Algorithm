# <IDEA>
# 1. 총 2의 ^ (배열길이) 만큼의 경우의 수가 생김
#     - 전부다 for문을 돌릴 수도 없는 노릇임
#     - 타겟넘버는 양수이므로 모두 -가 되는 경우의 수는 없음
# 그래프 탐색 아이디어, nonlocal 

def solution(numbers, target):
    answer = 0
    n = len(numbers)
    
    # 재귀함수 ()
    def dfs(idx, result):
        # idx n까지 왔으면 (0 ~ n-1까지 탐색 완료)
        if idx == n:
            if result == target:
                # answer이 전역번수가 아니므로 global이 아닌 nonlocal 사용
                nonlocal answer
                answer += 1
            return
        
        # idx n-1 이하이면 계속 탐색
        else:
            dfs(idx+1, result+numbers[idx])
            dfs(idx+1, result-numbers[idx])
            
    dfs(0,0)
    return answer